#!/usr/bin/env python

from socket import *
import subprocess
import time

sk = socket()
address = ('127.0.0.1',8900)
sk.bind(address)

sk.listen(3)

while True:
    print('waitting connection...')
    conn,addr = sk.accept()
    print(addr)
    while True:
        data = conn.recv(1024)
        obj = subprocess.Popen(data.decode('utf8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        cmd_error = obj.stderr.read()
        result_len = len(cmd_result)
	
        conn.send(str(result_len).encode('utf8'))
        conn.recv(1024) # zhan bao
        conn.send(cmd_result)
        conn.send(cmd_error)
    conn.close()
sk.close()
