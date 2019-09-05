from period import Period
from beforebed import BeforeBed
from bedtomidnight import BedToMidnight
from midnighttoend import MidnightToEnd



class Night:

    beforeBed = None
    bedToMidnight = None
    midnightToEnd = None

    def __init__(self, start=5, bedtime=9, end=4):

        assert(start >= 5 or start < 4)
        assert(end <= 4 or end > 5)

        if start < 4:
            self.midnightToEnd = MidnightToEnd(start=start,end=end)
        if end > 4 and end < bedtime:
            self.beforeBed = BeforeBed(start=start, end=end)
        else:
            self.beforeBed = BeforeBed(start=start, end=bedtime)
            self.bedToMidnight = BedToMidnight(start=bedtime, end=end)

            if end > 4 and end < 12:
                self.midnightToEnd = Period(rate=0)
            else:
                self.midnightToEnd = MidnightToEnd(end=end)


    def earnings(self):
        # print("-----")
        # print(str(self.beforeBed.duration()) + "," + str(self.beforeBed.value()))
        # print(str(self.bedToMidnight.duration()) + "," + str(self.bedToMidnight.value()))
        # print(str(self.midnightToEnd.duration()) + "," + str(self.midnightToEnd.value()))
        sum = 0
        if not self.beforeBed is None:
            sum = sum + self.beforeBed.value()
        if not self.bedToMidnight is None:
            sum = sum + self.bedToMidnight.value()
        if not self.midnightToEnd is None:
            sum = sum + self.midnightToEnd.value()

        return sum
