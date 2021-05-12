from Month import *

class Year:
    def __init__(self,year=None):
        if year == None:
            self.year = 1984
        else:
            self.year = year
        self.months = {}
        for i in range(1,13):
            self.months.update({i:Month(i)})
