import datetime
from Event import *
class Day:
    def __init__(self,day=None):
        if day == None:
            self.day = 1
        else:
            self.day = day
        self.eventMap = {}
        for i in range(24):
            self.eventMap.update({i:None})

    def getEventByHour(self,hour):
        return self.eventMap.get(hour)

    def addEvent(self,e):
        startTime = e.getStartTime()
        endTime = e.getEndTime()
        duration = e.getDuration().hour
        if duration < 1:
            duration = 1
        currentHour = startTime.hour
        for i in range(duration):
            self.eventMap.update({currentHour:e})
            currentHour += 1
        print("event successfully added")
        print("contents of eventMap:")

    def printDay(self):
        previousEvent = None
        for i in self.eventMap:
            e = self.eventMap.get(i)
            if i >= 10:
                if e == previousEvent or e == None:
                    print(f"{i}:00")
                else:
                    print(f"{i}:00 - {e}")
                    previousEvent = e
            else:
                if e == previousEvent:
                    print(f" {i}:00")
                else:
                    print(f"{i}:00 - {e}")
                    previousEvent = e

    def __repr__(self):
        return f"Day object with day#{self.day}"

    def save(self):
        saveString = "DAY:{self.day}:EVENTS:[\n"
        for i in self.eventMap:



if __name__ == '__main__':
    d = Day()
    e = Event("Jam","Jam in Joe's garage - bring an amp",datetime.time(17,00,00),datetime.time(22,00,00))
    d.addEvent(e)
    d.addEvent(e)
    d.printDay()
