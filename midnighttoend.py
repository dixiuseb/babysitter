from period import Period



class MidnightToEnd(Period):

    def __init__(self, start=12, end=1):
        assert(end <= 4)
        assert(start == 12 or start < 4)
        rate = 16
        super(MidnightToEnd, self).__init__(start=start,end=end,rate=16)
