import ticketstate


class selection(ticketstate):

    def selectzone(self, number):
        if number == 0:
            return "700 select zone complete" + "your zone is "+self.zone[number]
        elif number == 1:
            return "700 select zone complete" + "your zone is "+self.zone[number]
        elif number == 2:
            return "700 select zone complete" + "your zone is "+self.zone[number]
        elif number == 3:
            return "700 select zone complete" + "your zone is "+self.zone[number]
        else:
            return "709 Invalid zone"

    def selectdate(self, number):
        if number == 0:
            return "700 select date complete" + "your date is "+self.dateList[number]
        elif number == 1:
            return "700 select date complete" + "your date is "+self.dateList[number]
        elif number == 2:
            return "700 select date complete" + "your date is "+self.dateList[number]
        elif number == 3:
            return "700 select date complete" + "your date is "+self.dateList[number]
        else:
            return "709 Invalid date"

    def selecttime(self, number):
        if number == 0:
            return "700 select time complete" + "your time is "+self.time[number]
        elif number == 1:
            return "700 select time complete" + "your time is "+self.time[number]
        elif number == 2:
            return "700 select time complete" + "your time is "+self.time[number]
        elif number == 3:
            return "700 select time complete" + "your time is "+self.time[number]
        else:
            return "709 Invalid time"

