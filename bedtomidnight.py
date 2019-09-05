from period import Period



class BedToMidnight(Period):

    def __init__(self, start=6):
        assert(start >= 6 and start < 12)
        self.start = start

        self.end = 12
        self.rate = 8

    
