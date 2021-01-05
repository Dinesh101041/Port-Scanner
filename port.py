# sokect programming helps to connect two nodes on network to commuunicate with each other
import socket
# threading help us to perfrom mulitple task
import threading
# queue data strcuture helps to acessmultiplrthread
from queue import Queue


# the ip address that you want to scan 127.0.0.1 is localhost
target="127.0.0.1"
queue=Queue()
# list for ports
open_ports=[]

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

    #  mode 3 to scan the important ports 2
    # 20-	FTP Protocol (data) - port for transferring FTP data
    # 21-FTP Protocol (control) - port for FTP commands and flow control
    # 22-SSH (Secure Shell) - used for secure logins, file transfers (scp, sftp) and port forwarding
    # 23-Telnet protocol 
    # 25-SMTP (Simple Mail Transport Protocol)
    # 53-DNS (Domain Name System)
    # 80-HTTP (HyperText Transfer Protocol)
    # 110-POP3 (Post Office Protocol version 3)
    # 443-HTTPS 
     
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    # mode 4 we can enter the our choice port
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

# get the ports from the queue ant to print it
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        # if you also want to display closed ports uncomment the below lines
        # else:
            # print("Port {} is closed!".format(port))          



# fun to run the scan with two parameter threads is to amount of thread to start and mode reprresent type of mode
def run_scanner(threads, mode):

    # get the fuction of modes
    get_ports(mode)

    thread_list = []


    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)              

# 100- amount of thread  1 - type of mode
run_scanner(100, 1)
