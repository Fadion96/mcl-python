import unittest

from mcl.curve_type import CurveType
from mcl.mcl import mcl_init
from mcl.g1 import G1
from mcl.fr import Fr

class G1Tests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)

    def testAdd(self):
        gen = G1.BLS12_381_G1_generator()
        self.assertEqual(gen + gen, gen.double())

    def testSub(self):
        gen = G1.BLS12_381_G1_generator()
        self.assertEqual(gen.double() - gen, gen)

    def testMul(self):
        gen = G1.BLS12_381_G1_generator()
        self.assertEqual(gen * Fr(2), gen.double())


    def testIsZero(self):
        gen = G1.BLS12_381_G1_generator()
        P = G1()
        P.clear()
        self.assertTrue(P.is_zero())
        self.assertFalse(gen.is_zero())    

    def testEq(self):
        gen = G1.BLS12_381_G1_generator()
        self.assertTrue(gen == gen)
        self.assertFalse(gen.double() == gen)

    def testNeq(self):
        gen = G1.BLS12_381_G1_generator()
        self.assertTrue(gen != gen.double())
        self.assertFalse(gen != gen)

    def testGetStr(self):
        P = G1()
        P.clear()
        self.assertEqual(P.getStr(), "0")
        self.assertEqual(G1.BLS12_381_G1_generator().getStr(),
        "1 3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507 1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569")
        
    def testHashAndMapToG1(self):
        self.assertEqual(G1.hashAndMapToG1("test").getStr(),
        "1 1664126500441530256482751269291290703962889676827426721113973279626206305626152966034740921719739598015047469980014 2770511850529075397457134371943688177934498111089053025052575225110555843257818577745559532770169098874656481355098")