import datetime
class Event:
    def __init__(self,name=None,desc=None,startTime=None,endTime=None):
        if name == None:
            self.name = ""
        else:
            self.name = name
        if desc == None:
            self.desc = ""
        else:
            self.desc = desc
        if startTime == None:
            self.startTime = datetime.time()
        else:
            self.startTime = startTime
        if endTime == None:
            self.endTime = datetime.time()
        else:
            self.endTime = endTime


    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def setName(self,name):
        self.name = name

    def setDesc(self,desc):
        self.desc = desc

    def setStartTime(self,startTime):
        self.startTime = startTime

    def setEndTime(self,endTime):
        self.endTime = endTime

    def getDuration(self):
        minutes = self.endTime.minute - self.startTime.minute
        hours = 0
        if minutes < 0:
            minutes *= -1
            hours += 1
        hours = self.endTime.hour - self.startTime.hour
        return datetime.time(hours,minutes,0)

    def __repr__(self):
        return f"{self.name} : {self.startTime} - {self.endTime} - {self.desc}"

    def save(self):
        return f"EVENT:{self.name}:{self.desc}:{self.startTime}:{self.endTime}"


if __name__ == '__main__':
    e = Event("Jam","Jam in Joe's garage - bring an amp",datetime.time(17,00,00),datetime.time(22,00,00))
    print(e)
