from period import Period



class BedToMidnight(Period):

    def __init__(self, start=6, end=12):

        assert(start>=6 or start < 4)
        assert(end > start or end <= 4)
        if end < 4:
            end = 12

        rate = 8
        if start < 4:
            rate = 0

        super(BedToMidnight, self).__init__(start=start,end=end,rate=rate)

        # assert(start >= 6 and start < 12)
        # self.start = start
