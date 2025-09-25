
'''
Esta atividade consiste em implementar em Python a comunicação TCP
utilizando a interface socket. O intuito desta atividade é demostrar o
funcionamento do protocolo TCP, bem como as portas são mapeadas aos
processos por meio da interface socket
'''

'''
Um socket é basicamente um endpoint que estabelece uma conexão estável na internet
Existem 2 tipo de SOCKETS

- STREAM -> Utiliza comunicação TCP/IP, garante a chegada de dados, sem duplicação simultaneamente

- DATAGRAM -> Utiliza comunicação UDP, apenas manda os dados, não garante a chegada das mensagens nem de duplicação

vamos usar o SOCKET STREAM, no python se referimos a ele como:
            -socket.sock_stream
'''

import socket
import sys

# Hardcode information like PORT and HOST

HOST = "127.0.0.1" # localhost
PORT = "12345"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind the socket to a PORT
    try:
        s.bind((HOST,PORT))
    except:
        print("Error on binding the socket to a PORT")
        sys.exit()
    
    # now we need to listen for connections
    s.listen(5)
    print(f"Listening for connections on PORT: {PORT}")
    conn, addr = s.accept() # the socket now as conn is waiting for connections
    with conn as c:
        print(f"Connection established with {addr}")
        # now we can receive data from the client
        while True:
            data = c.recv(1024) # buffer size is 1024 bytes
            if not data: # sinalizes a empty packet, meaning the client closed the connection
                break # so we break the connection loop
            print(f"Received data: {data.decode()}")
            c.sendall(data) # echo back the received data
    print("Client closed the connection")
    conn.close()

