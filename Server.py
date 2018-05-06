import socket
import sys



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


def socket_bind():
    try:
        global host
        global port
        global s
        print("Bind socket to the host" + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error message: " + str(msg) + "\n" + "Retrying")
        socket_bind()

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP" + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()



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

# This function will call all staffs
def main():
    socker_ctreate()
    socket_bind()
    socket_accept()


main()
