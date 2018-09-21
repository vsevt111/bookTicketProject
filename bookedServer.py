import sys
import socket
import movie
import database
from clientRegister import *
import userstate
import ticketstate
import selection
from _thread import *


clientRegister = clientRegister()
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5565
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host,port))


def signup(conn):
    conn.send("""    ============ Sign Up =============
    Pleas Enter Your Prefer Username : """.encode('utf-8'))
    username=conn.recv(2048).decode('utf-8')
    conn.send("Please Enter Your Prefer Password : ".encode('utf-8'))
    password=conn.recv(2048).decode('utf-8')
    conn.send(clientRegister.signup(username,password).encode('utf-8'))
    print("Sign Up User : "+username+" Password : "+password)
    return


def login(conn):
    conn.send("Enter your Username".encode('utf-8'))
    username=conn.recv(2048).decode('utf-8')
    conn.send("Enter your Password".encode('utf-8'))
    password=conn.recv(2048).decode('utf-8')
    clientRegister.login(username,password)
    print(username+'login')

def switch(x,conn,loginState):
    if (x=='s'):
        signup(conn)
        return
    elif (x=='l'):
        login(conn)
    else:
        return
    
#Maximum number of connection that server will accept
serversocket.listen(5)
print('waiting')

#process that will run in every connection
def threaded_client (conn):
    loginState = False
    while (True):
        if(loginState==False):
            conn.sendall("""Welcome, 
            [l]ogin
            [s]ign up
            [q]uit   """.encode('utf-8'))
            switch1=conn.recv(2048).decode('utf-8')
            if(switch1=='q'):
                break
            switch(switch1,conn,loginState)
    conn.close()

#Start Servers
while True:
    conn, addr = serversocket.accept()
    print('connected to : '+addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,))