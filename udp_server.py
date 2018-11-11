# 1.验证空消息
# 2.验证大数据发送

from socket import *
import subprocess
import struct
buffer_size = 1024

sk = socket(AF_INET,SOCK_DGRAM)
address = ('127.0.0.1',8080)
sk.bind(address)
print('服务端启动。。')
while True:

    cmd,addr = sk.recvfrom(1024)


    obj = subprocess.Popen(cmd.decode('utf8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    err = obj.stderr.read()
    if err:
        cmd_res = err
    else:
        cmd_res = obj.stdout.read()

    head_bytes = struct.pack('i',len(cmd_res))
    print(head_bytes)
    sk.sendto(head_bytes,addr)
    sk.sendto(cmd_res,addr)
