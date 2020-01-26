from __future__ import annotations
import ctypes
from .curve_type import CurveType
from .g1 import G1
from .g2 import G2
from .gt import GT

MCLBN_FR_UNIT_SIZE = 4
MCLBN_FP_UNIT_SIZE = 6

FR_SIZE = MCLBN_FR_UNIT_SIZE
G1_SIZE = MCLBN_FP_UNIT_SIZE * 3
G2_SIZE = MCLBN_FP_UNIT_SIZE * 6
GT_SIZE = MCLBN_FP_UNIT_SIZE * 12
MCLBN_COMPILED_TIME_VAR = (MCLBN_FR_UNIT_SIZE * 10) + MCLBN_FP_UNIT_SIZE

mcl = ctypes.CDLL("libmcl.so", mode = ctypes.RTLD_GLOBAL)
mcl = ctypes.CDLL("libmclbn384_256.so")

def mcl_init(curve_type: CurveType):
    ret = mcl.mclBn_init(curve_type.value, MCLBN_COMPILED_TIME_VAR)
    if ret:
        raise RuntimeError(f'Init error: {ret}')

def pairing(g1: G1, g2: G2) -> GT:
    ret = GT()
    mcl.mclBn_pairing(ctypes.byref(ret.v), ctypes.byref(g1.v), ctypes.byref(g2.v))
    return ret