import socket

serversocket = socket.socket(socket. AF_INET , socket. SOCK_DGRAM )

host = '127.0.0.1'
port = 7777
server_address = ( ('127.0.0.1' , 7777 ))
print ( 'Server waiting for connection' )

socket.bind(server_address)

def math (message):

message = message.split( ',' )

operation = message[ 0]
variable1 = int(message[ 1])
variable2 = int(message[ 2 ])

if operation == '1' :
    return variable1 + variable2
elif operation == '2' :
    return variable1 - variable2
elif operation == '3' :
    return variable1 * variable2
elif operation == '4' :
    return variable1 / variable2
elif operation == '5' :
    return variable1 % variable2
else:
     print (''PLEASE USE A VALID OPERARION ( 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division or 5 for modulus)" )

while True :
print ('waiting for a connection...' )

client_message, client_address = socket.recvfrom( 1024 *3 )

result = str (math(client_message))

socket.sendto(result, client_address)

print ('Result sent!' )