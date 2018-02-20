

import socket

serversocket = socket.socket(socket. AF_INET , socket. SOCK_DGRAM )

message = []

operation = input ('''
Net-Centric Mathematics Server
Please select a maths operation to perform:
1 - Addidtion
2 - Subtraction
3 - Multiplication
4 - Division
5 - Modulus
>_
'''
)

message.append( str (operation))

variable1 = input ('enter the first value: >_ ' )
variable2 = input ('enter the second value: >_ ' )

message.append( str (variable1))
message.append( str (variable2))

message = ',' .join(message)

socket.sendto(message,( '127.0.0.1' , 7777))

server_result, server_address = socket.recvfrom( 3096 )
print ( 'server result: ' + server_result)

socket.close() ;



