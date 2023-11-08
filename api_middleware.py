#from colabcode import ColabCode
from fastapi import FastAPI
import uvicorn
import socket

#cc = ColabCode(port=12000, code=False)

app = FastAPI()

def client_program(query: str):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5069  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    client_socket.send(query.encode())  # send message
    data = client_socket.recv(4096).decode()

    client_socket.close()  # close the connection

    return data

@app.get("/")
##async def read_root():
def read_root():
  return {"message": "Analisis de algoritmos"}

@app.get("/query/{query}")
#http://localhost/query/esta%20es%20la%20query
##async def read_root():
def execute_query(query):
  data = client_program(query)
  #data = "asdf"
  return {"query": f"Query lista: {query}", "response": f"{data}"}

uvicorn.run(app, host="127.0.0.1", port=12000)

#ngrok
#cc.run_app(app=app)

## si no se ocupa colabcode usar la siguiente linea en consola:
## uvicorn.exe main:app --reload