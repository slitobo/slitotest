import socket

cs = socket.socket()
address=('127.0.0.1',8080)
cs.connect(address)
print(cs)
while True:

    inp = input('>>>')
    cs.send(bytes(inp,'utf-8'))
    if inp == 'bye':
        break
    data = cs.recv(1024)
    print(data.decode('utf8'))
cs.close()
