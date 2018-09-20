class Movie:
    name=0
    seatLeft=5    
    seatTaken=['1','2','3','4','5']
    
    def __init__ (self,name):
        self.name  = name
    
    def printSeat(self):
        seat = ''
        for i in range (0,4):
            seat+='['+self.seatTaken[i]+'] '
        return seat
    
    def takeSeat(self,position):
        position-=1
        self.seatTaken[position]='X'
    

    
    
