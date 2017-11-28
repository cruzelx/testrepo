import os, sys, socket, _thread
if len(sys.argv) != 3:
    print('''
    Usage: script hostname port\n
    ''')
    sys.exit()
HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
BUFF_SIZE = 2**15
CONN_LIST = []
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
except socket.gaierror as error:
    print("socket couldn't be created due to error: %s" %(error))
    sys.exit()
s.bind((HOST,PORT))
s.listen(100)
CONN_LIST.append(s)
 
def runBarryrun(conn,addr):
    conn.send("welcome fellow human!!! \n")
    while 1:
        try:
            msg = conn.recv(BUFF_SIZE)
            if msg:
                spread(conn,"\n<"+addr[0]+">"+msg+"\n")
            else:
                if conn in CONN_LIST:
                    CONN_LIST.remove(conn)
                
        except:
            continue



def spread(conn,msg):
    for con in CONN_LIST:
        if con != conn:
            try:
                con.sendall(msg)
            except:
                con.close()
                if con in CONN_LIST:
                    CONN_LIST.remove(con)


while 1:
    conn, addr = s.accept()
    CONN_LIST.append(conn)
    print("(%s:%s) connected" %(addr[0]:addr[1]))
    _thread.start_new_thread(runBarryrun,(conn,addr))
s.close()
conn.close()


