class ticketstate:
    amountTicket = [200, 150, 500, 250]
    time = ['10.00-12.00', '13.00-15.00', '16.00-18.00', '19.00-21.00']
    zone = ['A', 'B', 'C', 'D']
    dateList = ['15', '23', '25', '1']
    verifyTicket = False
    def __init__(self):
        verifyTicket = False

    def booking(self, dates):
        if dates in self.dateList:
            i = 0
            while self.dateList[i] != dates:
                i = i + 1
            self.amountTicket[i] = self.amountTicket[i] - 1
            return "700 booking complete. date" + self.dateList[i] + "have " + str(self.amountTicket[i])
        else:
            return "750 fail to booking"

    def cancel(self, dates):
        if dates in self.dateList:
            i = 0
            while self.dateList[i] != dates:
                i = i + 1
                self.amountTicket[i] = self.amountTicket[i] + 1
            return "700 cancel complete" + str(self.amountTicket[i])
        else:
            return "750 fail to cancel"

    def showstatus(self):
        return "600 status of all concert"


