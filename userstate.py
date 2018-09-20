from database import database


class Userstate(database):
    loginboolean = False
    name = ''
    password = ''

    def login(self, name, password):
        if self.clientDictionary.get(name, '0') != '0' and self.clientDictionary.get(name) == password:
            self.loginboolean = True
            self.loginList.append(name)
            return "700 log in complete"
        else:
            return "750 fail to log in. You may not sign up."

    def logout(self, name):
        if name in self.loginList:
            self.loginboolean = False
            self.loginList.remove(name)
            return "700 log out complete"
        else:
            return "705 interrupt with other"
