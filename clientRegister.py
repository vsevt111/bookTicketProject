clientList = []
moneyList = 0
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


def signup(name):
    if name not in clientList:
        clientList.append(name)
        return "700 sign up complete"
    else:
        return "750 fail to sign up because this username have been in database"

def submoney(client,money):
    if client in clientList:
        i = 0
        while clientList[i] != client:
            i += 1
        moneyList[i] -= money
        return "700 add your money complete"+moneyList[i]
    else:
        return "750 your account have not be log in or not enough money"

def status(name):
    if name in clientList:
        i = 0
        while name != clientList[i]:
            i+=1
        return "600 show your status"+name+"\n"+"MONEY:"+moneyList[i]
    else:
        return "750 fail to show your status because this username have been in database"