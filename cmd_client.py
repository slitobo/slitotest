#!/usr/bin/env python

from socket import *
import subprocess

cs = socket()
address = ('127.0.0.1',8900)
cs.connect(address)

while True:
    inp = input('>>>').encode('utf8')
    if not inp:
        #print('input is null key')
        continue
    cs.send(inp)
    
    result_len = cs.recv(1024)
    cs.send(b'nianbao')
    data = bytes()
    result_len = int(str(result_len,'utf8'))
    print(result_len,type(result_len))
    #zhanbao = cs.recv(1024)
    while len(data) != result_len:
        print('recv length is :',len(data))
        recv = cs.recv(1024)    
        data += recv
    print(data.decode('utf8'))
