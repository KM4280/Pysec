import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

server.bind((host, port))
server.listen(5)

print("host =",host,"port =",port)
client, address = server.accept()

while True:
    print("Connection recieved from", client, address)
    message = input("-> ")
    if message == "exit":
        client.close()
        print("Closed TCP with", client, address)
    
    client.send(message.encode('ascii'))
    print("Sent to", host, port)
    response = client.recv(1024).decode()
    print(response)
	
