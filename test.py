import unittest

from period import Period

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

        with self.assertRaises(TypeError):
            c = Period(start="time", end=10, rate=10)

        with self.assertRaises(AssertionError):
            c = Period(start=1, end=0, rate=10)

        with self.assertRaises(AssertionError):
            c = Period(start=1, end=13, rate=10)

        with self.assertRaises(TypeError):
            c = Period(start=1, end="time", rate=10)

    def test_duration(self):
        a = Period(start=5, end=9)
        self.assertEqual(a.relativeTime(5), 5)
        self.assertEqual(a.relativeTime(9), 9)
        self.assertEqual(a.duration(), 4)


if __name__ == '__main__':
    unittest.main()
