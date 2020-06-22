import sys
import numba


@numba.jit("i8(i8)")
def recur(t):
    if t == 0:
        return 1
    return t * recur(t - 1)


if sys.argv[-1] == "-c":
    # numba compile
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('recur', 'i8(i8)')(recur)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    from my_module import recur
    print(recur(5))
