from period import Period



class MidnightToEnd(Period):

    def __init__(self, start=5, end=12):
        assert(end <= 4 and end > 0)
        self.end = end

        self.start = 12
        self.rate = 16
