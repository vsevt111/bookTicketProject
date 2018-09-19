import clientRegister

dateList = ['15', '23', '25', '1']
amount = [200, 150, 500, 250]
place = ['place X', 'place Y', 'place Z', 'place ZZ']

def booking(dates):
    if dates in dateList:
        i = 0
        while dateList[i] != dates:
            i = i+1
        amount[i] = amount[i]-1
    return "700 booking complete. date"+dateList[i]+"have"+amount[i]

def cancel(dates):
    if dates in dateList:
        i = 0
        while dateList[i] != dates:
            i = i+1
        amount[i] = amount[i]+1
    return "700 cancel complete"+amount[i]

def verify():
    clientRegister.verify = True

def showstatus():
    return "600 status of all concert"

