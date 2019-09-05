from beforebed import BeforeBed
from bedtomidnight import BedToMidnight
from midnighttoend import MidnightToEnd



class Night:

    beforeBed = None
    bedToMidnight = None
    midnightToEnd = None

    def __init__(self, start=5, bedtime=9, end=4):
        assert()
        self.beforeBed = BefordBed(start=5, end=bedtime)
        self.bedToMidnight = BedToMidnight(start=bedtime)
        self.midnightToEnd = MidnightToEnd(end=end)
