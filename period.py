



class Period:

    start=0;
    end=0;
    rate=0;

    def __init__(self, start=1, end=1, rate=0):
        assert(start >= 1 and start <= 12)
        self.start = start
        assert(end >= 1 and end <= 12)
        self.end = end
        assert(rate >= 0)
        self.rate = rate


    def duration(self):
        return self.relativeTime(self.end) - self.relativeTime(self.start)


    def relativeTime(self, time):
        return time if time > 4 else 12 + time
