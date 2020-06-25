import sys
import numpy as np


def solve():
    "void()"
    xs = np.zeros(1, dtype=np.int32)
    xs_p = 0

    def xs_push(v):
        nonlocal xs, xs_p
        if xs_p == xs.size:
            # equivalent of `xs.resize(xs.size * 2)`
            old = xs
            xs = np.zeros(xs.size * 2, dtype=xs.dtype)
            xs[:old.size] = old
            # ---
        xs[xs_p] = v
        xs_p += 1

    for i in range(100):
        xs_push(i)

    print(xs)


def main():
    solve()


def _test():
    import doctest
    doctest.testmod()


USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
    # cc.export('main', 'i8[:](i8,i8,i8[::1])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :], contiguous array[::1]
    cc.compile()
    exit()
else:
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read

    if (USE_NUMBA and sys.argv[-1] != '-p') or sys.argv[-1] == "--numba":
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import solve  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
