
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

# Vamos criar um objeto para armazenar nosso socket
server_socket = socket.SOCK_STREAM