from __future__ import annotations
from .lib import mcl
from .consts import FR_SIZE
from typing import Optional
import ctypes

class Fr(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * FR_SIZE)]

    def __init__(self, v: Optional[str, int]=None) -> None:
        if isinstance(v, int):
            self.setInt(v)
        elif isinstance(v, str):
            self.setStr(v)
    
    def setInt(self, v: int) -> None:
        mcl.mclBnFr_setInt(ctypes.byref(self.v), v)
    
    def setStr(self, s: str) -> None:
        mcl.mclBnFr_setStr(ctypes.byref(self.v), 
                            ctypes.c_char_p(s.encode()),
                            len(s), 10
                            )
    def getStr(self) -> str:
        buf_len = 1024
        buf = ctypes.create_string_buffer(buf_len)
        mcl.mclBnFr_getStr(buf, len(buf), ctypes.byref(self.v), 10)
        return buf.value.decode()
    
    def __str__(self) -> str:
        return self.getStr()

    def add(self, rhs: Fr) -> Fr:
        ret = Fr()
        mcl.mclBnFr_add(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __add__(self, rhs: Fr) -> Fr:
        return self.add(rhs)

    def sub(self, rhs: Fr) -> Fr:
        ret = Fr()
        mcl.mclBnFr_sub(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret
    
    def __sub__(self, rhs: Fr) -> Fr:
        return self.sub(rhs)

    def mul(self, rhs: Fr) -> Fr:
        ret = Fr()
        mcl.mclBnFr_mul(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __mul__(self, rhs: Fr) -> Fr:
        return self.mul(rhs)

    def div(self, rhs: Fr) -> Fr:
        ret = Fr()
        mcl.mclBnFr_div(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __truediv__(self, rhs: Fr) -> Fr:
        return self.div(rhs)

    def is_zero(self) -> bool:
        return mcl.mclBnFr_isZero(ctypes.byref(self.v)) != 0

    def is_one(self) -> bool:
        return mcl.mclBnFr_isOne(ctypes.byref(self.v)) != 0

    def __eq__(self, rhs: Fr) -> bool:
        return mcl.mclBnFr_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) != 0

    def __ne__(self, rhs: Fr) -> bool:
        return mcl.mclBnFr_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) == 0

    def set_by_CSPRNG(self) -> None:
        mcl.mclBnFr_setByCSPRNG(ctypes.byref(self.v))
