from enum import Enum
from Day import *
class Months(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
class Month:
    def __init__(self,month=None):
        self.month = month
        self.monthDict = {Months.JANUARY:31,Months.FEBRUARY:28,Months.MARCH:31,Months.APRIL:30,Months.MAY:31,Months.JUNE:30,Months.JULY:31,Months.AUGUST:31,Months.SEPTEMBER:30,Months.OCTOBER:31,Months.NOVEMBER:30,Months.DECEMBER:31}
        self.dayList = []
        if self.month in self.monthDict:
            for i in monthDict.get(self.month):
                self.dayList[i] = Day()

    def getDays(self):
        if self.month in self.monthDict:
            return self.monthDict.get(self.month)


#test main
if __name__ == '__main__':
    m = Month(Months.JANUARY)
    print(m.getDays())
