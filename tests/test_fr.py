import unittest

from mcl import mcl_init, Fr, CurveType

class FrTests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)

    def testAdd(self):
        self.assertEqual(Fr(10) + Fr(10), Fr(20))

    def testSub(self):
        self.assertEqual(Fr(20) - Fr(10), Fr(10))

    def testMul(self):
        self.assertEqual(Fr(20) * Fr(10), Fr(200))

    def testDiv(self):
        self.assertEqual(Fr(20) / Fr(10), Fr(2))

    def testIsZero(self):
        self.assertTrue(Fr(0).is_zero())
        self.assertFalse(Fr(1).is_zero())
    
    def testIsOne(self):
        self.assertTrue(Fr(1).is_one())
        self.assertFalse(Fr(2).is_one())

    def testEq(self):
        self.assertTrue(Fr(5) == Fr(5))
        self.assertFalse(Fr(6) == Fr(5))

    def testNeq(self):
        self.assertTrue(Fr(6) != Fr(5))
        self.assertFalse(Fr(5) != Fr(5))

    def testGetStr(self):
        self.assertEqual(Fr("10").getStr(), "10")

    def testClear(self):
        a = Fr()
        a.clear()
        self.assertEqual(a, Fr(0))

    def testInv(self):
        a = Fr(10)
        a_inv = a.inv()
        self.assertEqual(a, a_inv.inv())

    def testIsNegative(self):
        self.assertTrue(Fr(-1).is_negative())
        self.assertFalse(Fr(1).is_negative())

    def testIsOdd(self):
        self.assertTrue(Fr(1).is_odd())
        self.assertFalse(Fr(2).is_odd())

    def testSerialize(self):
        a = Fr(10)
        a_bytes = a.serialize()
        self.assertEqual(a, Fr.deserialize(a_bytes))

    def testNeg(self):
        a = Fr(10)
        a_neg = a.neg()
        self.assertEqual(a, a_neg.neg())

    def testSqr(self):
        a = Fr(10)
        self.assertEqual(Fr(100), a.sqr())