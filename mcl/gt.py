from __future__ import annotations
from .lib import mcl
from .consts import GT_SIZE
from .fr import Fr
from typing import Optional
import ctypes


class GT(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * GT_SIZE)]

    def __init__(self, s: Optional[str]=None) -> None:
        if isinstance(s, str):
            self.setStr(s)

    def setStr(self, s: str) -> None:
        mcl.mclBnGT_setStr(ctypes.byref(self.v), ctypes.c_char_p(s.encode()), len(s), 10)

    def getStr(self) -> str:
        buf_len = 1024
        buf = ctypes.create_string_buffer(buf_len)
        mcl.mclBnGT_getStr(buf, len(buf), ctypes.byref(self.v), 10)
        return buf.value.decode()

    def __str__(self) -> str:
        return self.getStr()

    def neg(self) -> GT:
        ret = GT()
        mcl.mclBnGT_neg(ctypes.byref(ret.v), ctypes.byref(self.v))
        return ret
    
    def __neg__(self) -> GT:
        return self.neg()

    def sub(self, rhs: GT) -> GT:
        ret = GT()
        mcl.mclBnGT_sub(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __sub__(self, rhs: GT) -> GT:
        return self.sub(rhs)

    def add(self, rhs: GT) -> GT:
        ret = GT()
        mcl.mclBnGT_add(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __add__(self, rhs: GT) -> GT:
        return self.add(rhs)

    def mul(self, fr: Fr) -> GT:
        ret = GT()
        mcl.mclBnGT_mul(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(fr.v))
        return ret

    def __mul__(self, fr: Fr) -> GT:
        return self.mul(fr)

    __rmul__ = __mul__

    def eq(self, rhs: GT) -> GT:
        return mcl.mclBnGT_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) != 0

    def __eq__(self, rhs: GT) -> GT:
        return self.eq(rhs)

    def ne(self, rhs: GT) -> GT:
        return mcl.mclBnGT_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) == 0
    
    def __ne__(self, rhs: GT) -> GT:
        return self.ne(rhs)

    def is_zero(self) -> bool:
        return mcl.mclBnGT_isZero(ctypes.byref(self.v)) != 0

    def is_one(self) ->bool:
        return mcl.mclBnGT_isOne(ctypes.byref(self.v)) != 0

    def clear(self) -> None:
        mcl.mclBnGT_clear(ctypes.byref(self.v))
    