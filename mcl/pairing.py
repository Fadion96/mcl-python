from __future__ import annotations
import ctypes
from .mcl import mcl
from .g1 import G1
from .g2 import G2
from .gt import GT

def pairing(g1: G1, g2: G2) -> GT:
    ret = GT()
    mcl.mclBn_pairing(ctypes.byref(ret.v), ctypes.byref(g1.v), ctypes.byref(g2.v))
    return ret