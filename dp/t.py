#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
#import numpy as np
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7

debug_indent = 0


def debug(*x):
    global debug_indent
    x = list(x)
    indent = 0
    if x[0].startswith("enter") or x[0][0] == ">":
        indent = 1
    if x[0].startswith("leave") or x[0][0] == "<":
        debug_indent -= 1
    x[0] = "  " * debug_indent + x[0]
    print(*x, file=sys.stderr)
    debug_indent += indent


def solve(N, lessthan):
    k = 1
    table = [0] * (k + 1)
    if lessthan[-1]:
        for i in range(k + 1):
            table[i] = k - i
    else:
        for i in range(k + 1):
            table[i] = i

    for k in range(2, N):
        newtable = [0] * (k + 1)
        if lessthan[-k]:
            for i in range(k + 1):
                for j in range(k - i):
                    newtable[i] += table[j + i]
        else:
            for i in range(k + 1):
                for j in range(i):
                    newtable[i] += table[j]
        table = [x % MOD for x in newtable]
    return sum(table) % MOD


def main():
    # parse input
    N = int(input())
    lessthan = [c == ord("<") for c in input().strip()]
    print(solve(N, lessthan))


# tests
T0 = """
2
>
"""


def test_T0():
    """
    >>> as_input(T0)
    >>> main()
    1
    """


T01 = """
3
<<
"""


def test_T01():
    """
    >>> as_input(T01)
    >>> main()
    1
    """


T02 = """
3
>>
"""


def test_T02():
    """
    >>> as_input(T02)
    >>> main()
    1
    """


T03 = """
3
<>
"""


def test_T03():
    """
    >>> as_input(T03)
    >>> main()
    2
    """


T1 = """
4
<><
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    5
    """


T2 = """
5
<<<<
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    1
    """


T3 = """
20
>>>><>>><>><>>><<>>
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    217136290
    """
# add tests above


def _test():
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())

    def input():
        return bytes(f.readline(), "ascii")

    def read():
        return bytes(f.read(), "ascii")


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
        print("testing")
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
