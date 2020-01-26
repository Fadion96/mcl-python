import unittest

from mcl import mcl_init, Fr, CurveType, G2

class G2Tests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)

    def testAdd(self):
        gen = G2.BLS12_381_G2_generator()
        self.assertEqual(gen + gen, gen.double())

    def testSub(self):
        gen = G2.BLS12_381_G2_generator()
        self.assertEqual(gen.double() - gen, gen)

    def testMul(self):
        gen = G2.BLS12_381_G2_generator()
        self.assertEqual(gen * Fr(2), gen.double())


    def testIsZero(self):
        gen = G2.BLS12_381_G2_generator()
        P = G2()
        P.clear()
        self.assertTrue(P.is_zero())
        self.assertFalse(gen.is_zero())    

    def testEq(self):
        gen = G2.BLS12_381_G2_generator()
        self.assertTrue(gen == gen)
        self.assertFalse(gen.double() == gen)

    def testNeq(self):
        gen = G2.BLS12_381_G2_generator()
        self.assertTrue(gen != gen.double())
        self.assertFalse(gen != gen)

    def testGetStr(self):
        P = G2()
        P.clear()
        self.assertEqual(P.getStr(), "0")
        self.assertEqual(G2.BLS12_381_G2_generator().getStr(),
        "1 352701069587466618187139116011060144890029952792775240219908644239793785735715026873347600343865175952761926303160 3059144344244213709971259814753781636986470325476647558659373206291635324768958432433509563104347017837885763365758 1985150602287291935568054521177171638300868978215655730859378665066344726373823718423869104263333984641494340347905 927553665492332455747201965776037880757740193453592970025027978793976877002675564980949289727957565575433344219582")
        
    def testHashAndMapToG2(self):
        self.assertEqual(G2.hashAndMapToG2("test").getStr(),
        "1 3035410284670172822278382403907957115899337120663486077801493809533423924318135197683333296400242994086357673794613 1785141689185704244408511370343548582455844354038743678281465122886880406332213470381122199452223171130208308480869 1368740321157085535728641591680992724049630704543547765519682150483834212857623630342844610363547815367196638166789 2757256452659599929159715569400251080685640247308155348704439120375220684577877691557778850755152690283407968072052")