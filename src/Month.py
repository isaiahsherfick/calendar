from enum import Enum
from Day import *
class Month:
    def __init__(self,month=None,leapYear=False):
        self.month = month
        if not leapYear:
            self.monthDict = {None:0,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        else:
            self.monthDict = {None:0,1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        self.dayList = []
        if self.month in self.monthDict:
            for i in range(1,self.monthDict.get(self.month)+1):
                self.dayList += [Day(i)]

    def getDays(self):
        if self.month in self.monthDict:
            return self.monthDict.get(self.month)

    def getDay(self,day):
        return self.dayList[day]

    def displayDayList(self):
        for d in self.dayList:
            print(d)

    def __repr__(self):
        return f"Month #{self.month}"


#test main
if __name__ == '__main__':
    #deprecated none of this works now
    m = Month(1)
    print(m.getDays())
    m.displayDayList()
    m=Month(2,True)
    print(m.getDays())
    m.displayDayList()
    m=Month(2)
    print(m.getDays())
    m.displayDayList()
