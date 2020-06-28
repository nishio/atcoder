#!/usr/bin/env python3

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
    for i in range(D):
        print(S[i].argmax() + 1)


def solve2(D, CS, S):
    "void()"
    last = [-1] * 26
    for i in range(D):
        dscore = np.zeros(26)
        for j in range(26):
            dscore[j] += S[i, j]
            dscore[j] -= sum(CS[k] * (i - last[k])
                             for k in range(26) if j != k)

        j = dscore.argmax()
        print(j + 1)
        last[j] = i


def solve3(D, CS, S):
    "void()"
    from time import perf_counter
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
    while perf_counter() - time < 1.5:
        answer = []
        last = [-1] * 26
        for i in range(D):
            dscore = np.zeros(26)
            if random() > 0.99:

                for j in range(26):
                    dscore[j] += S[i, j]
                    dscore[j] -= sum(CS[k] * (i - last[k])
                                     for k in range(26) if j != k)

                j = dscore.argmax()
            else:
                j = int(random() * 26)
            answer.append(j + 1)
            last[j] = i
        s = calcScore(answer, D, CS, S)
        if s > bestscore:
            bestscore = s
            debug(": bestscore", bestscore)
            bestanswer = answer
    print(*bestanswer, sep="\n")


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
    while perf_counter() - time < 10.5:
        answer = []
        last = [-1] * 26
        k1 = random()
        k2 = random() * k1
        S = ORIG_S.copy()
        S[:-1] = (S[:-1] + k1 * ORIG_S[1:]) / (1 + k1)
        S[:-2] = (S[:-2] + k2 * ORIG_S[2:]) / (1 + k2)
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


T = """
5
86 90 69 51 2 96 71 47 88 34 45 46 89 34 31 38 97 84 41 80 14 4 50 83 7 82
19771 12979 18912 10432 10544 12928 13403 3047 10527 9740 8100 92 2856 14730 1396 15905 6534 4650 11469 3628 8433 2994 10899 16396 18355 11424
6674 17707 13855 16407 12232 2886 11908 1705 5000 1537 10440 10711 4917 10770 17272 15364 19277 18094 3929 3705 7169 6159 18683 15410 9092 4570
6878 4239 19925 1799 375 9563 3445 5658 19857 11401 6997 6498 19933 3848 2426 2146 19745 16880 17773 18359 3921 14172 16730 11157 5439 256
8633 15862 15303 10749 18499 7792 10317 5901 9395 11433 3514 3959 5202 19850 19469 9790 5653 784 18500 10552 17975 16615 7852 197 8471 7452
19855 17918 7990 10572 4333 438 9140 9104 12622 4985 12319 4028 19922 12132 16259 17476 2976 547 19195 19830 16285 4806 4471 9457 2864 2192
"""

OUT = """
1
17
13
14
13
"""


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
