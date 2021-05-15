from Month import *

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

class Year:
    def __init__(self,year=None):
        if year == None:
            self.year = 1984
        else:
            self.year = year
        self.months = {}
        for i in range(1,13):
            if isLeapYear(self.year):
                self.months.update({i:Month(i,True)})
            else:
                self.months.update({i:Month(i,False)})
                pass
        #for i in self.months:
            #print(f"{i} : {self.months.get(i)}")

    def getMonth(self,month):
        return self.months.get(month)

    def isLeapYear(self):
        return isLeapYear(self.year)



if __name__ == '__main__':
    #for i in range(2000,2022):
        #print(f"{i} is a leap year: {isLeapYear(i)}")

    y = Year(2020)
    print(y.getMonth(4))
    print(y.getMonth(5).getDay(17))

