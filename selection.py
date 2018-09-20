import ticketstate


class selection(ticketstate):
    def selectplace(self, number):
        if number == 0:
            return "700 select place complete" + self.place[number]
        elif number == 1:
            return "700 select place complete" + self.place[number]
        elif number == 2:
            return "700 select place complete" + self.place[number]
        elif number == 3:
            return "700 select place complete" + self.place[number]
        else:
            return "709 Invalid place"

    def selectzone(self, number):
        if number == 0:
            return "700 select place complete" + self.zone[number]
        elif number == 1:
            return "700 select place complete" + self.zone[number]
        elif number == 2:
            return "700 select place complete" + self.zone[number]
        elif number == 3:
            return "700 select place complete" + self.zone[number]
        else:
            return "709 Invalid zone"

    def selectdate(self, number):
        if number == 0:
            return "700 select place complete" + self.dateList[number]
        elif number == 1:
            return "700 select place complete" + self.dateList[number]
        elif number == 2:
            return "700 select place complete" + self.dateList[number]
        elif number == 3:
            return "700 select place complete" + self.dateList[number]
        else:
            return "709 Invalid date"

    def selecttime(self, number):
        if number == 0:
            return "700 select place complete" + self.time[number]
        elif number == 1:
            return "700 select place complete" + self.time[number]
        elif number == 2:
            return "700 select place complete" + self.time[number]
        elif number == 3:
            return "700 select place complete" + self.time[number]
        else:
            return "709 Invalid time"
