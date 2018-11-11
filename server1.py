# import subprocess
# #
# #
# #
# # while 1:
# #     inp = input('>>>')
# #
# #     obj = subprocess.Popen(inp,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# #     cmd_out = obj.stdout.read()
# #     cmd_error = obj.stderr.read()
# #
# #     print('------',str(cmd_error,'gbk'))
# #     print(str(cmd_out,'gbk'))


# tcp 长连接
#
# import socket
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# address = ('127.0.0.1',8888)
# sk.bind(address)
#
# sk.listen(3)
#
# while True:
#     print('waitting for connection...')
#     conn,addr = sk.accept()
#     print('Current conn is:',addr)
#     while True:
#         # 客户端先关闭连接时，
#         # try:
#         #     data = conn.recv(1024)
#         # except  ConnectionAbortedError as e:
#         #     print('客户端主动关闭，丢失连接')
#         #     print(e)
#         #     break
#
#         # 接收数据
#         data = conn.recv(1024)
#         data = str(data,'utf-8')
#         if data == 'bye':
#             print('客户端关闭连接')
#             break
#         else:
#             print(data)
#
#         # 发送数据
#         inp = input('>>>')
#         if inp == 'bye':
#             conn.send(bytes(inp, 'utf-8'))
#             break
#         else:
#             conn.send(bytes(inp,'utf-8'))
#
#     conn.close()
# sk.close()

# udp 连接
#
# from socket import *
#
# sk = socket(type=SOCK_DGRAM)
# addr = ('127.0.0.1',8080)
# sk.bind(addr)
#
# while True:
#     msg,addr = sk.recvfrom(1024)
#     print(addr)
#     print(msg.decode('utf8'))
#
#     inp = input('>>>').encode('utf8')
#     sk.sendto(inp,addr)
#     if inp == 'bye':
#         break
# sk.close()
from socket import *
sk = socket()
addr = ('127.0.0.1',8090)
sk.bind(addr)
sk.listen(3)
print('waitting...')
conn,addr=sk.accept()
conn.send(b'hello')
conn.send(b'world')

conn.close()
sk.close()
#
# while True:
#     sk.listen(3)
#     print('waitting for connection')
#     conn,addr=sk.accept()
#     print(addr)
#
#     while True:
#         data = conn.recv(1024)
#         print(data.decode('utf-8'))
#
#         if not data:
#             print('null key')
#             break
#
#         obj = subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
#         cmd_result = obj.stdout.read()
#         result_len = len(cmd_result)
#         print(result_len)
#
#         conn.send(bytes(str(result_len),'utf8'))
#         conn.send(cmd_result)


        # print(str(cmd_result,'gbk'))
        # cmd_error = obj.stderr.read()















