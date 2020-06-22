import sys
import numpy as np
P = 998244353


def main(N, S, AS):
    DP = np.zeros((S + 1, N + 1), dtype=np.int64)
    DP[0, 0] = 1
    # print(DP)

    for i in range(N):
        for j in range(S + 1):
            v = DP[j, i] * 2
            if AS[i] <= j:
                v += DP[j - AS[i], i]
            DP[j, i + 1] = v % P

    # print(DP)
    print(DP[S, N])


if sys.argv[-1] == 'ONLINE_JUDGE':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'void(i8,i8,i8[:])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    # read parameter
    N, S = map(int, input().split())
    AS = np.array(list(map(int, input().split())))
    from my_module import main
    main(N, S, AS)
