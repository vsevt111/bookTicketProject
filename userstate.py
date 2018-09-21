from database import *
class Userstate(database):
    loginboolean = False
    name = ''
    password = ''

    def __init__(self,name,password):
        self.name=name
        self.password=password
    def login(self, name, password):
        if self.clientDictionary.get(name, '0') != '0' and self.clientDictionary.get(name) == password:
            self.loginboolean = True
            self.loginList.append(name)
            return "log in complete"
        else:
            return "fail to log in. You may not sign up. Or Incorrect Password"


    def logout(self, name):
        if name in self.loginList:
            self.loginboolean = False
            self.loginList.remove(name)
            return "log out complete"
        else:
            return "interrupt with other"
