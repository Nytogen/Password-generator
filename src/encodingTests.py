import encoding
import unittest

class ceaserShift(unittest.TestCase):
    def testEn(self):
        self.assertEqual(encoding.ceaserShiftEn("012345678", 1), "123456789")
        self.assertEqual(encoding.ceaserShiftEn("123456789", -1), "012345678")
        self.assertEqual(encoding.ceaserShiftEn("Hello", 5), "Mjqqt")
        self.assertEqual(encoding.ceaserShiftEn("Hello", -3), "Ebiil")

    def testDe(self):
        self.assertEqual(encoding.ceaserShiftDe("123456789", 1), "012345678")
        self.assertEqual(encoding.ceaserShiftDe("012345678", -1), "123456789")
        self.assertEqual(encoding.ceaserShiftDe("Mjqqt", 5), "Hello")
        self.assertEqual(encoding.ceaserShiftDe("Ebiil", -3), "Hello")

class rot13(unittest.TestCase):
    def testEn(self):
        self.assertEqual(encoding.rot13En("abc"), "nop")

    def testDe(self):
        self.assertEqual(encoding.rot13De("nop"), "abc")


if __name__ == "__main__":
    unittest.main()