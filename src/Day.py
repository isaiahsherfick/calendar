
class Day:
    def __init__(self,day=None):
        if day == None:
            self.day = 1
        else:
            self.day = day
        self.eventMap = {}
        for i in range(24):
            self.eventMap.update({i:None})

    def getEventByHour(hour):
        return
    def __repr__(self):
        return f"Day object with day#{self.day}"

