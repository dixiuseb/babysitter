import unittest

from period import Period
from beforebed import BeforeBed
from bedtomidnight import BedToMidnight
from midnighttoend import MidnightToEnd
from night import Night

class TestStringMethods(unittest.TestCase):

    def test_period_ctor(self):
        a = Period()
        self.assertEqual(a.start, 1)
        self.assertEqual(a.end,  1)
        self.assertEqual(a.rate, 0)

        b = Period(start=5, end=10, rate=10)
        self.assertEqual(b.start, 5)
        self.assertEqual(b.end,  10)
        self.assertEqual(b.rate, 10)

        with self.assertRaises(AssertionError):
            c = Period(start=0, end=10, rate=10)

        with self.assertRaises(AssertionError):
            c = Period(start=13, end=10, rate=10)

        with self.assertRaises(AssertionError):
            c = Period(start="time", end=10, rate=10)

        with self.assertRaises(AssertionError):
            c = Period(start=1, end=0, rate=10)

        with self.assertRaises(AssertionError):
            c = Period(start=1, end=13, rate=10)

        with self.assertRaises(AssertionError):
            c = Period(start=1, end="time", rate=10)

    def test_duration(self):
        a = Period(start=5, end=9)
        self.assertEqual(a.relativeTime(5), 5)
        self.assertEqual(a.relativeTime(9), 9)
        self.assertEqual(a.duration(), 4)


    def test_BeforeBed(self):
        with self.assertRaises(AssertionError):
            a = BeforeBed(start=4, end=9)

        with self.assertRaises(AssertionError):
            a = BeforeBed(start=5, end=4)

        with self.assertRaises(AssertionError):
            a = BeforeBed(start=7, end=7)

        a = BeforeBed(start=5, end=7)
        self.assertEqual(a.value(), 24)

    def test_BedToMidnight(self):
        with self.assertRaises(AssertionError):
            a = BedToMidnight(start=5)

        with self.assertRaises(AssertionError):
            a = BedToMidnight(start=12)

        a = BedToMidnight(start=1)
        self.assertEqual(a.value(), 0)

        a = BedToMidnight(start=6)
        self.assertEqual(a.value(), 48)

    def test_MidnightToEnd(self):
        with self.assertRaises(AssertionError):
            a = MidnightToEnd(end=-1)

        with self.assertRaises(AssertionError):
            a = MidnightToEnd(end=12)

        with self.assertRaises(AssertionError):
            a = MidnightToEnd(end=5)

        with self.assertRaises(AssertionError):
            a = MidnightToEnd(end=13)

        a = MidnightToEnd(end=3)
        self.assertEqual(a.value(), 48)

    def testNight(self):
        with self.assertRaises(AssertionError):
            a = Night(start=4)

        with self.assertRaises(AssertionError):
            a = Night(bedtime=4)

        with self.assertRaises(AssertionError):
            a = Night(end=5)

        with self.assertRaises(AssertionError):
            a = Night(start=5, bedtime=5)

        with self.assertRaises(AssertionError):
            a = Night(bedtime=11, end=12)

        with self.assertRaises(AssertionError):
            a = Night(bedtime=11, end=5)

        a = Night(start=7, bedtime=11, end=3)
        self.assertEqual(a.earnings(), 104)

        a = Night(start=7, bedtime=8, end=9)
        self.assertEqual(a.earnings(), 20)

        a = Night(start=7, bedtime=10, end=8)
        self.assertEqual(a.earnings(), 12)

        a = Night(start=7, bedtime=1, end=4)
        self.assertEqual(a.earnings(), 124)

if __name__ == '__main__':
    unittest.main()
