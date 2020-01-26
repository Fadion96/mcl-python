from __future__ import annotations
from .mcl import G2_SIZE, mcl
from .fr import Fr
from typing import Optional
import ctypes


class G2(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * G2_SIZE)]

    def __init__(self, s: Optional[str]=None) -> None:
        if isinstance(s, str):
            self.setStr(s)

    def setStr(self, s: str) -> None:
        mcl.mclBnG2_setStr(ctypes.byref(self.v), ctypes.c_char_p(s.encode()), len(s), 10)

    def getStr(self) -> str:
        buf_len = 1024
        buf = ctypes.create_string_buffer(buf_len)
        mcl.mclBnG2_getStr(buf, len(buf), ctypes.byref(self.v), 10)
        return buf.value.decode()

    def __str__(self) -> str:
        return self.getStr()

    def neg(self) -> G2:
        ret = G2()
        mcl.mclBnG2_neg(ctypes.byref(ret.v), ctypes.byref(self.v))
        return ret
    
    def __neg__(self) -> G2:
        return self.neg()

    def sub(self, rhs: G2) -> G2:
        ret = G2()
        mcl.mclBnG2_sub(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __sub__(self, rhs: G2) -> G2:
        return self.sub(rhs)

    def add(self, rhs: G2) -> G2:
        ret = G2()
        mcl.mclBnG2_add(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v))
        return ret

    def __add__(self, rhs: G2) -> G2:
        return self.add(rhs)

    def mul(self, fr: Fr) -> G2:
        ret = G2()
        mcl.mclBnG2_mul(ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(fr.v))
        return ret

    def __mul__(self, fr: Fr) -> G2:
        return self.mul(fr)

    __rmul__ = __mul__

    def double(self) -> G2:
        ret = G2()
        mcl.mclBnG2_dbl(ctypes.byref(ret.v), ctypes.byref(self.v))
        return ret

    def eq(self, rhs: G2) -> G2:
        return mcl.mclBnG2_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) != 0

    def __eq__(self, rhs: G2) -> G2:
        return self.eq(rhs)

    def ne(self, rhs: G2) -> G2:
        return mcl.mclBnG2_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) == 0
    
    def __ne__(self, rhs: G2) -> G2:
        return self.ne(rhs)

    def is_zero(self) -> bool:
        return mcl.mclBnG2_isZero(ctypes.byref(self.v)) != 0

    def clear(self) -> None:
        mcl.mclBnG2_clear(ctypes.byref(self.v))
    
    @staticmethod
    def hashAndMapToG2(s: str) -> G2:
        ret = G2()
        buf = ctypes.create_string_buffer(s.encode())
        mcl.mclBnG2_hashAndMapTo(ctypes.byref(ret.v), buf, len(buf))
        return ret

    @staticmethod
    def BLS12_381_G2_generator() -> G2:
        ret = G2("1 352701069587466618187139116011060144890029952792775240219908644239793785735715026873347600343865175952761926303160 3059144344244213709971259814753781636986470325476647558659373206291635324768958432433509563104347017837885763365758 1985150602287291935568054521177171638300868978215655730859378665066344726373823718423869104263333984641494340347905 927553665492332455747201965776037880757740193453592970025027978793976877002675564980949289727957565575433344219582")
        return ret