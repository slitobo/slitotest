import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is: ',self.request)
        print('addr is:',self.client_address)

        while True:
            #收消息
            data = self.request.recv(1024)
            print('收到客户端的消息：',data)

            #发消息
            self.request.sendall(data.upper())

if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1',8080),Myserver)
    #s = socketserver.ForkingTCPServer(('127.0.0.1',8080),Myserver)
    s.serve_forever()
