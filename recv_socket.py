#!/usr/bin/python
#-*-coding:utf-8-*-

import socket 
import struct

# data of socket and file datapath 
ADDR = ('',7757)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')

def Reveiver_File_Server(recvSock):

    recvSock.listen(20)

    conn,addr = recvSock.accept()

    fhead = conn.recv(FILEINFO_SIZE)
    filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
    print filename,temp1,filesize,temp2
    print filename,len(filename),type(filename)
    print filesize
    print filename

    filename = filename.strip('\00') #...
    fp = open(filename,'wb')
    restsize = filesize

    while 1:
        if restsize > BUFSIZE:
            filedata = conn.recv(BUFSIZE)
        else:
            filedata = conn.recv(restsize)
        if not filedata: 
            break
        fp.write(filedata)
        restsize = restsize-len(filedata)
        if restsize == 0:
            break
    fp.close()

if __name__ == '__main__':
	  recvSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    recvSock.bind(ADDR)
    while 1:
        Reveiver_File_Server(recvSock)


