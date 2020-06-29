#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys
import numpy as np
from random import random
from time import time as perf_counter

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(D, CS, S):
    "i8[:](i8,i8[:],i8[:,:])"
    def calcScore(answer, D, CS, S):
        last = [-1] * 26
        score = 0
        for i in range(D):
            j = answer[i] - 1
            score += S[i, j]
            last[j] = i
            for j in range(26):
                score -= CS[j] * (i - last[j])

        return score

    answer = []
    last = [-1] * 26
    for i in range(D):
        dscore = np.zeros(26)
        for j in range(26):
            dscore[j] += S[i, j]
            for k in range(26):
                if j != k:
                    dscore[j] -= CS[k] * (i - last[k])

        j = dscore.argmax()
        answer.append(j + 1)
        last[j] = i
    s = calcScore(answer, D, CS, S)

    bestscore = s
    bestanswer = answer

    for _trial in range(1000):
        answer = []
        last = [-1] * 26
        k1 = random() * 0.1
        k2 = random()
        F = S.copy()
        F[:-1] = F[:-1] - np.int64(k1 * S[1:])
        F[:-2] = F[:-2] - np.int64(k2 * S[2:])
        for i in range(D):
            dscore = np.zeros(26)
            for j in range(26):
                dscore[j] += F[i, j]
                for k in range(26):
                    if j != k:
                        dscore[j] -= CS[k] * (i - last[k])

            j = dscore.argmax()
            answer.append(j + 1)
            last[j] = i
        s = calcScore(answer, D, CS, S)
        if s > bestscore:
            #debug("bestscore: k1,k2", k1, k2)
            bestscore = s
            bestanswer = answer
    return np.array(bestanswer)


# def solve():
#     print([1] * 26, set="\n")


def main():
    D = int(input())
    CS = np.array(list(map(int, input().split())))
    S = np.int16(read().split())
    S = S.reshape((D, 26))

    print(*solve(D, CS, S), sep="\n")


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


USE_NUMBA = True
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
