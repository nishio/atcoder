import sys
import numba


def main(x):
    # NG
    # def recur(t):
    #     if t == 0:
    #         return 1
    #     return t * recur(t - 1)

    # OK
    def recur(t):
        return 1
    return recur(x)


if sys.argv[-1] == "-c":
    # numba compile
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8)')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    from my_module import main
    print(main(5))
