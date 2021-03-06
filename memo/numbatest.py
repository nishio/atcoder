import sys
import numba
import numpy as np


def main(xs):
    ret = 0
    a = {}
    for x in xs:
        a[x] = ret
        ret += x
    return ret


if sys.argv[-1] == "-c":
    # numba compile
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8[:])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    from my_module import main
    print(main(np.array(range(10))))
