import socket



# 默认是 family=AF_INET, type=SOCK_STREAM
# type:
# SOCK_STREAM : TCP
# SOCK_Dgram: UDP

# family
# family=AF_INET :服务器之间的通信
# family=AF_UNIX : unix 不同进程间的通信

# 1) 创建socket，使用默认参数

# ss = socket.socket()
#
# # 2) 为socket绑定ip地址和端口
#
# address=('127.0.0.1',8000)
# ss.bind(address)
#
# # 3) 设置监听端口客户端等待连接数
# ss.listen(3) # 容纳排队连接数
#
# # 4) 设置等待,并接收cs
#
# print('waiting for connection...')
# cs,addr = ss.accept() # 客户端的socket
# print(ss)
# print(cs) # (<socket.socket fd=728, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 57831)>, ('127.0.0.1', 57831))
#
# # server 发送
# inp = input('>>>')
# cs.send(bytes(inp,'utf8'))

# server 接受

# data = conn.recv(1024)
#
# print(data)

#
# ss = socket.socket()
# address = ('127.0.0.1',8000)
# ss.bind(address)
# ss.listen(2)
# print('waitting for connection...')
#
# while True:
#     cs, addr = ss.accept()
#
#     while True:
#         try:
#             data = cs.recv(1024)
#         except Exception:
#             break
#         if not data: break
#         print('......',str(data,'utf8'))
#         inp = input('>>>')
#         if inp == 'q': break
#         cs.send(bytes(inp,'utf8'))
#
# ss.close()

# import subprocess
# while True:
#     inp = input('>>>')
#     cmd_res = subprocess.Popen(inp,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#
#
#     err = cmd_res.stderr.read()
#
#     out = cmd_res.stdout.read()
#
#     print('err:',err.decode('gbk'))
#     print(len(err))
#
#     print(out.decode('gbk'))

from socket import *
sk = socket()
addr = ('127.0.0.1',8090)
sk.connect(addr)

data1 = sk.recv(1024)
print(data1.decode('utf8'))
data2 = sk.recv(1024)
print(data2.decode('utf8'))


sk.close()
