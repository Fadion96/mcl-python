from __future__ import annotations
import ctypes
from .curve_type import CurveType


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
