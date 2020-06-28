#!/usr/bin/env python3
"""
best submitted
https://atcoder.jp/contests/intro-heuristics/submissions/14819677
"""
from collections import defaultdict
from heapq import heappush, heappop
import sys
import numpy as np
from random import random
from time import perf_counter

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(D, CS, S):
    "void()"
    time = perf_counter()

    answer = []
    last = [-1] * 26
    for i in range(D):
        dscore = np.zeros(26)
        for j in range(26):
            dscore[j] += S[i, j]
            dscore[j] -= sum(CS[k] * (i - last[k])
                             for k in range(26) if j != k)

        j = dscore.argmax()
        answer.append(j + 1)
        last[j] = i
    s = calcScore(answer, D, CS, S)

    bestscore = s
    bestanswer = answer

    ORIG_S = S.astype(np.float)
    while perf_counter() - time < 1.5:
        answer = []
        last = [-1] * 26
        k1 = random() * 0.1
        k2 = random()
        S = ORIG_S.copy()
        S[:-1] = S[:-1] - k1 * ORIG_S[1:]
        S[:-2] = S[:-2] - k2 * ORIG_S[2:]
        for i in range(D):
            dscore = np.zeros(26)
            for j in range(26):
                dscore[j] += S[i, j]
                dscore[j] -= sum(CS[k] * (i - last[k])
                                 for k in range(26) if j != k)

            j = dscore.argmax()
            answer.append(j + 1)
            last[j] = i
        s = calcScore(answer, D, CS, ORIG_S)
        if s > bestscore:
            #debug("bestscore: k1,k2", k1, k2)
            bestscore = s
            bestanswer = answer
    print(*bestanswer, sep="\n")


def calcScore(answer, D, CS, S):
    last = [-1] * 26
    score = 0
    for i in range(D):
        j = answer[i] - 1
        score += S[i, j]
        last[j] = i
        score -= sum(CS[j] * (i - last[j]) for j in range(26))
    return score


# def solve():
#     print([1] * 26, set="\n")


def main():
    D = int(input())
    CS = list(map(int, input().split()))
    S = np.int16(read().split())
    S = S.reshape((D, 26))

    # print(calcScore(answer, D, CS, S))
    solve(D, CS, S)


def _test():
    import doctest
    doctest.testmod()
    as_input(T)
    main()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())
    input = f.readline
    read = f.read


USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
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
