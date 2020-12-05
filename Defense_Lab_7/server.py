import socket

HOST = '127.0.0.1'
PORT = 8081 
server = socket.socket()
server.bind((HOST, PORT))
print('Server is up...')
print('Listening for Client connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'{client_addr} Client is connected')
print('To stop server type "stop server"')
while True:
    command = input('Input cmd command : ')
    if command == "stop server":
        exit(0)
    command = command.encode()
    try:
        client.send(command)
        print('Command is sent. Awaiting response...')
        output = client.recv(1024)
        output = output.decode()
        print(f"Output: {output}")
    except Exception as e:
        print(e)
