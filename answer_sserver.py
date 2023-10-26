from classes.inverted_list import InvertedList
import socket

def load_index():
    index = InvertedList()
    index.load_index("data/index.txt")

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = "respuesta generica"
        conn.send(data.encode())
        conn, address = server_socket.accept()

    conn.close()


if __name__ == '__main__':
    load_index()
    server_program()