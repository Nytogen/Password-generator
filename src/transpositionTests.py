import transposition
import unittest

class railFence(unittest.TestCase):
    def testEn(self):
        self.assertEqual(transposition.railFenceEn("1234567890", 2, False),"1357924680")
        self.assertEqual(transposition.railFenceEn("1234567890", 3, False), "1592468037")
        self.assertEqual(transposition.railFenceEn("1234567890", 4, True), ["17","268","359","40"])
        self.assertEqual(transposition.railFenceEn("1234567890", 5, True), ["19","280","37","46","5"])


if __name__ == "__main__":
    unittest.main()