import sys, socket, select
if len(sys.argv) != 3:
    print('''
    Usage: scriptfile host port'''
    )
    sys.exit()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.gaierror:
    print("Couldn't create socket...")
    sys.exit()

HOST = str(sys.argv[0])
PORT = int(sys.argv[1])
BUFF_SIZE = 2**15
s.connect((HOST,PORT))

while 1:
    CONN_LIST = [s]
    read,write,error = socket.socket(CONN_LIST,[],[])
    for sock in read:
        if sock == s:
            msg = sock.recv(BUFF_SIZE)
            print(msg)
        else:
            msg = sys.stdin.readline()
            s.send(msg)
            sys.stdout.write("\n< you >: ")
            sys.stdout.write(msg)
            sys.stdout.flush()
s.close()






