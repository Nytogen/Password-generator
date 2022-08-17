import transposition
import unittest

class railFence(unittest.TestCase):
    def testEn(self):
        self.assertEqual(transposition.railFenceEn("1234567890", 2),"1357924680")
        self.assertEqual(transposition.railFenceEn("1234567890", 3), "1592468037")
        self.assertEqual(transposition.railFenceEn("1234567890", 4), "1726835940")
        self.assertEqual(transposition.railFenceEn("1234567890", 5), "1928037465")


if __name__ == "__main__":
    unittest.main()