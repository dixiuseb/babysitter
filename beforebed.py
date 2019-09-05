from period import Period



class BeforeBed(Period):

    def __init__(self, start=5, end=12):
        assert(start >= 5 or start < 4)
        assert(end > start or end < 4)
        if end < 4:
            end = 12
        super(BeforeBed, self).__init__(start=start,end=end,rate=12)
