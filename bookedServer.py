from sys            import *
from socket         import *         
from movie          import *         
from database       import *           
from userstate      import *            
from ticketstate    import *                 
from selection      import *       
from clientRegister import *
from _thread        import *


person = clientRegister()
serversocket = socket(AF_INET,SOCK_STREAM)
host = ''
port = 5565
serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serversocket.bind((host,port))


def signup(conn):
    conn.send("""    ============ Sign Up =============
    Pleas Enter Your Prefer Username : """.encode('utf-8'))
    username=conn.recv(2048).decode('utf-8')
    conn.send("Please Enter Your Prefer Password : ".encode('utf-8'))
    password=conn.recv(2048).decode('utf-8')
    conn.send(person.signup(username,password).encode('utf-8'))
    print("Sign Up User : "+username+" Password : "+password)
    return False


def login(conn):
    conn.send("Enter your Username".encode('utf-8'))
    username=conn.recv(2048).decode('utf-8')
    conn.send("Enter your Password".encode('utf-8'))
    password=conn.recv(2048).decode('utf-8')
    loginStatus=person.login(username,password)
    conn.send(loginStatus.encode('utf-8'))
    if loginStatus=="log in complete":
        print(username+'login')
        return True
    else:
        print(username+' login Rejected')
        return False

def switch(x,conn):
    if (x=='s'):
        return signup(conn)
        
    elif (x=='l'):
        return login(conn)
        
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
            conn.send(
            """Welcome, 
            [l]ogin
            [s]ign up
            [q]uit   """.encode('utf-8'))
            switch1=conn.recv(2048).decode('utf-8')
            if(switch1=='q'):
                break
            loginState = switch(switch1,conn)
        elif loginState==True:
            conn.send(
                """What you want to do today?
            [b]uy ticket
            [l]ogout""".encode('utf-8'))
            switch1=conn.recv(2048).decode('')
            

    conn.close()

#Start Servers
while True:
    conn, addr = serversocket.accept()
    print('connected to : '+addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,))