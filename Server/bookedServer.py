import sys
import socket
import movie
from _thread import *

movie1 = movie.Movie("Friday 13th")
movie2 = movie.Movie("Your Name")
movie3 = movie.Movie("Star Wars: The Last Jedi")
movieList=[movie1,movie2,movie3]
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5565
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host,port))

def switch(x,conn):
    return {
        # 'b' : movieChoose(conn),
        'q' : conn.close()
    }.get(x)
    
#Maximum number of connection that server will accept
serversocket.listen(5)
print('waiting')

#process that will run in every connection
def threaded_client (conn):
    while (True):
        conn.sendall("Welcome what you want to do? : [b]uy ticket [c]ancel")
        switch(conn.recv(1024).decode('utf-8'),conn)
    conn.close()

#Start Servers
while True:
    conn, addr = serversocket.accept()
    print('connected to : '+addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,))