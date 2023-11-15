from classes.inverted_list import InvertedList
import socket

index = InvertedList()

def load_index():
    index.load_index("data/index.txt")
    index.load_doclen("data/document_len.txt")
    #print("index load [OK]")
    #print(index)

#def make_query(query):
#    response = str()
#    for word in query:
#        response += str(index.find(word))

#    return response

def make_query(query):
    words = query.split()
    intersection_list = index.find(words[0])
    for word in words[1:]:
        intersection_list = index.query_or(intersection_list, word)

    sorted_index = intersection_list.get_full_index_sorted()

    return str(sorted_index)

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5069  

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))

        data = make_query(str(data))
        print(f"response: {data}")

        #data = "respuesta generica"
        conn.send(str(data).encode())

    conn.close()

if __name__ == '__main__':
    load_index()
    server_program()