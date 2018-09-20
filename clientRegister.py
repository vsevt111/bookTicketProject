<<<<<<< HEAD
clientList = []
moneyList = []
ticketAmount = 0
verify = False
def addmoney(client,money):
    if client in clientList:
        i = 0
        while clientList[i] != client:
            i += 1
        moneyList[i] += money
        return "700 add your money complete"+moneyList[i]
    else:
        return "750 your account have not be log in"
=======
from Userstate import Userstate
from ticketstate import ticketstate
>>>>>>> master


class clientRegister(Userstate, ticketstate):
    def __init__(self):
        self.ticketAmount = 0
        self.verifyTicket = False

    def addmoney(self, client, money):
        if self.loginboolean:
            self.moneyDictionary[client] = self.moneyDictionary.get(client) + money
            return "700 add your money complete"
        else:
            return "750 your account have not be log in"

    def submoney(self, client, money):
        if self.loginboolean:
            if self.moneyDictionary.get(client) - money >= 0:
                self.moneyDictionary[client] = self.moneyDictionary.get(client) - money
                return "700 add your money complete"
            else:
                return "750 fail to substract money ."
        else:
            return "750 your account have not be log in "

    def status(self,name):
        if self.loginboolean:
            return "600 show your status" + name + "\n" + "MONEY:" + str(self.moneyDictionary.get(name))
        else:
            return "750 fail to show your status"

    def verify(self, client, money):
        self.verifyTicket = True
        self.submoney(client, money)
        return "700 vertify complete. Thank you"
