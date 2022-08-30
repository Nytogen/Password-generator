import transposition
import unittest

class redFence(unittest.TestCase):
    def testEn(self):
        self.assertEqual(transposition.redFenceEn("1234567890", "12", False),"1357924680")
        self.assertEqual(transposition.redFenceEn("1234567890", "132", False), "1593724680")
        self.assertEqual(transposition.redFenceEn("1234567890", "1234", True), ["17","268","359","40"])
        self.assertEqual(transposition.redFenceEn("1234567890", "54321", True), ["5","46","37","280","19"])

    def testDe(self):
        self.assertEqual(transposition.redFenceDe("1357924680", "12"),"1234567890")
        self.assertEqual(transposition.redFenceDe("1593724680", "132"), "1234567890")
        self.assertEqual(transposition.redFenceDe("1726835940", "1234"), "1234567890")
        self.assertEqual(transposition.redFenceDe("5463728019", "54321"), "1234567890")           

class railFence(unittest.TestCase):
    def testEn(self):
        self.assertEqual(transposition.railFenceEn("1234567890", 2, False),"1357924680")
        self.assertEqual(transposition.railFenceEn("1234567890", 3, False), "1592468037")
        self.assertEqual(transposition.railFenceEn("1234567890", 4, True), ["17","268","359","40"])
        self.assertEqual(transposition.railFenceEn("1234567890", 5, True), ["19","280","37","46","5"])

    def testDe(self):
        self.assertEqual(transposition.railFenceDe("1357924680", 2),"1234567890")
        self.assertEqual(transposition.railFenceDe("1592468037", 3), "1234567890")
        self.assertEqual(transposition.railFenceDe("1726835940", 4), "1234567890")
        self.assertEqual(transposition.railFenceDe("1928037465", 5), "1234567890")        

class completeColumnar(unittest.TestCase):
    def testEn(self):
        self.assertEqual(transposition.completeColumnarEn("thisisexampletext", "4312"), "iepesxlxhsmttiaet")
        self.assertEqual(transposition.completeColumnarEn("thisisexampletext", "1234"), "tiaethsmtiepesxlx")


if __name__ == "__main__":
    unittest.main()