import clientRegister

dateList = ['15', '23', '25', '1']
amount = [200, 150, 500, 250]
place = ['place X', 'place Y', 'place Z', 'place ZZ']
zone = ['A', 'B', 'C', 'D']

def booking(dates):
    if dates in dateList:
        i = 0
        while dateList[i] != dates:
            i = i+1
        amount[i] = amount[i]-1
        return "700 booking complete. date"+dateList[i]+"have"+amount[i]
    else:
        return "750 fail to booking"


def cancel(dates):
    if dates in dateList:
        i = 0
        while dateList[i] != dates:
            i = i+1
        amount[i] = amount[i]+1
        return "700 cancel complete"+amount[i]
    else:
        return "750 fail to cancel"

def verify(client,money):
    clientRegister.verify = True
    clientRegister.submoney(client, money)
    return "700 vertify complete. Thank you"

def showstatus():
    return "600 status of all concert"

