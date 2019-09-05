from period import Period



class BeforeBed(Period):

    def __init__(self, start=5, end=12):
        assert(start >= 5)
        self.start = start

        assert(end > start and end < 12)
        self.end = end

        self.rate = 12
