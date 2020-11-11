import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

VERSION = 1

def checkCheckSum(buff):
    r = 0
    for i in range(len(buff)-1):
        r = VERSION* (r + ord(buff[i]))
    r = r & 0xff
    return r

while True:
    data, addr = sock.recvfrom(1024)
    v = checkCheckSum(data)
    if(v == ord( data[len(data)-1])):
        print "valid"
    else:
        print "error"
    
