#!/usr/bin/python
#coding:utf-8

import socket 
import os
import sys
import struct

tar_name = sys.argv[1]

# data of socket and file datapath 
ADDR = ("ip",7757)
BUFSIZE = 1024
filename = tar_name 
FILEINFO_SIZE=struct.calcsize('128s32sI8s')

def Send_File_Client():
    sendSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sendSock.connect(ADDR)

    fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
    sendSock.send(fhead)
    fp = open(filename,'rb')

    while 1:
        filedata = fp.read(BUFSIZE)
        if not filedata: 
            break
        sendSock.send(filedata)

    fp.close()
    sendSock.close()

if __name__ == '__main__':
    Send_File_Client()

