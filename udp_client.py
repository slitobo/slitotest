# 1.验证空消息
# 2.验证大数据发送

from socket import *
import struct
buffer_size = 1024

sk = socket(AF_INET,SOCK_DGRAM)
address = ('127.0.0.1',8080)

while True:
    inp = input('>>>').encode('utf8')
    sk.sendto(inp,address)

    head_bytes,addr = sk.recvfrom(4)
    head_bytes_len = struct.unpack('i',head_bytes)[0]

    # 数据量小时使用
    # data,addr = sk.recvfrom(head_bytes_len)

    # 一般接受使用循环
    has_recv = bytes()
    while len(has_recv) != head_bytes_len:
        data,addr = sk.recvfrom(buffer_size)
        has_recv += data
		

    print(data.decode('utf8'),addr)
