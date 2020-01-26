from enum import Enum

class CurveType(Enum):
    MCL_BN254 = 0
    MCL_BN381_1 = 1
    MCL_BN381_2 = 2
    MCL_BN462 = 3
    MCL_BN_SNARK1 = 4
    MCL_BLS12_381 = 5
    MCL_BN160 = 6   