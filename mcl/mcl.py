from __future__ import annotations
from .lib import mcl
from .curve_type import CurveType
from .consts import MCLBN_COMPILED_TIME_VAR

def mcl_init(curve_type: CurveType):
    ret = mcl.mclBn_init(curve_type.value, MCLBN_COMPILED_TIME_VAR)
    if ret:
        raise RuntimeError(f'Init error: {ret}')