from __future__ import annotations
from .mcl import G1_SIZE, mcl
from .fr import Fr
from typing import Optional
import ctypes


class G1(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * G1_SIZE)]

    def __init__(self, s: Optional[str]=None) -> None:
        if isinstance(s, str):
            self.setStr(s)

    def setStr(self, s: str) -> None:
        mcl.mclBnG1_setStr(ctypes.byref(self.v), ctypes.c_char_p(s.encode()), len(s), 10)

    def getStr(self) -> str:
        buf_len = 1024
        buf = ctypes.create_string_buffer(buf_len)
        mcl.mclBnG1_getStr(buf, len(buf), ctypes.byref(self.v), 10)
        return buf.value.decode()

    def __str__(self) -> str:
        return self.getStr()

    def neg(self) -> G1:
        ret = G1()
        mcl.mclBnG1_neg(ctypes.byref(ret.v), ctypes.byref(self.v))
        return ret
    
    def __neg__(self) -> G1:
        return self.neg()

    def sub(self, rhs: G1) -> G1:
        ret = G1()
        mcl.mclBnG1_sub(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __sub__(self, rhs: G1) -> G1:
        return self.sub(rhs)

    def add(self, rhs: G1) -> G1:
        ret = G1()
        mcl.mclBnG1_add(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __add__(self, rhs: G1) -> G1:
        return self.add(rhs)

    def mul(self, fr: Fr) -> G1:
        ret = G1()
        mcl.mclBnG1_mul(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(fr.v))
        return ret

    def __mul__(self, fr: Fr) -> G1:
        return self.mul(fr)

    __rmul__ = __mul__

    def double(self) -> G1:
        ret = G1()
        mcl.mclBnG1_dbl(ctypes.byref(ret.v), ctypes.byref(self.v))
        return ret

    def eq(self, rhs: G1) -> G1:
        return mcl.mclBnG1_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) != 0

    def __eq__(self, rhs: G1) -> G1:
        return self.eq(rhs)

    def ne(self, rhs: G1) -> G1:
        return mcl.mclBnG1_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) == 0
    
    def __ne__(self, rhs: G1) -> G1:
        return self.ne(rhs)

    def is_zero(self) -> bool:
        return mcl.mclBnG1_isZero(ctypes.byref(self.v)) != 0

    def clear(self) -> None:
        mcl.mclBnG1_clear(ctypes.byref(self.v))
    
    @staticmethod
    def hashAndMapToG1(s: str) -> G1:
        ret = G1()
        buf = ctypes.create_string_buffer(s.encode())
        mcl.mclBnG1_hashAndMapTo(ctypes.byref(ret.v), buf, len(buf))
        return ret

    @staticmethod
    def BLS12_381_G1_generator() -> G1:
        ret = G1("1 \
            3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507 \
            1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569")
        return ret