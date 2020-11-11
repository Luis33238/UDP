import socket
import time as t
UDP_IP = '127.0.0.1'
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

i = 0

# des
# i, i+1, i*2


# RBT
HEAD      = "RBT"
MSG_TYPE  = "GET"
MSG_TYPE  = "ACK"
MSG_TYPE  = "SET" 
SEP       = " "

DATA_TYPE = "VEL"
DATA_TYPE = "POS"

# RBT SET VEL data TAIL
# VEL data0 data1
# data0 = mot number or "left" "right"
# data1 = vels (rad/sec)

VERSION = 1

def getCheckSum(buff):
    r = 0
    for i in range(len(buff)):
        r = VERSION * (r + ord(buff[i]))
    r = r & 0xff
    return r

while True:
    data = DATA_TYPE + SEP
    data = data + str(i) + SEP

    buff = HEAD + SEP
    buff = buff + MSG_TYPE + SEP
    buff = buff + data + SEP
    TAIL = getCheckSum(buff)
    buff = buff + chr(TAIL)

    i = i + 1
    sock.sendto(buff, (UDP_IP, UDP_PORT))
    print buff
    t.sleep(0.5)
