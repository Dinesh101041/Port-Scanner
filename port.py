# sokect programming helps to connect two nodes on network to commuunicate with each other
import socket
# threading help us to perfrom mulitple task
import threading
# queue data strcuture helps to acessmultiplrthread
from queue import Queue


# the ip address that you want to scan
target="127.0.0.1"
queue=Queue()
# list for ports
ports=[]

# setting up function
def portscan(port):
    try:
        # creating socket connection
        # if the port present it will return true other wise return false
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# the function to the possible ports
def get_ports(mode):
    # mode1 is to  scans the 1023 standard ports
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    #mode 2 is to scan the 49152 reserved ports 
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)
