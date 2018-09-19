import clientRegister
login=False
loginList=[]

def login(name):
    if name in clientRegister.clientList:
        loginList.append(name)
        login = True
        return "700 log in complete"
    else:
        return "750 fail to log in. You may not sign up."

def logout(name):
    if name in loginList:
        login = False
        loginList.remove(name)
        return "700 log out complete"
    else:
        return "705 interrupt with other"