#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
#import numpy as np
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 2 ** 31 - 1  # sys.maxsize # float("inf")
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


def set_depth(depth):
    global N, SEGTREE_SIZE, NONLEAF_SIZE
    N = depth
    SEGTREE_SIZE = 1 << N
    NONLEAF_SIZE = 1 << (N - 1)


def range_update(table, left, right, action):
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
    while left < right:
        if left & 1:
            table[left] = action(table[left])
            left += 1
        if right & 1:
            right -= 1
            table[right] = action(table[right])
        left //= 2
        right //= 2


def down_propagate_to_leaf(table, pos, binop, unity):
    pos += NONLEAF_SIZE
    down_propagate(table, pos, binop, unity)
    return table[pos]


def down_propagate(table, pos, binop, unity):
    for max_level in range(N):
        if 2 ** max_level > pos:
            max_level -= 1
            break
    for level in range(max_level):
        i = pos >> (max_level - level)

        table[i * 2] = binop(table[i], table[i * 2])
        table[i * 2 + 1] = binop(table[i], table[i * 2 + 1])
        table[i] = unity


def set_items(table, xs):
    for i, x in enumerate(xs, NONLEAF_SIZE):
        table[i] = x


def debugprint(xs, minsize=0, maxsize=None):
    strs = [str(x) for x in xs]
    if maxsize != None:
        for i in range(NONLEAF_SIZE, SEGTREE_SIZE):
            strs[i] = strs[i][:maxsize]
    s = max(len(s) for s in strs[NONLEAF_SIZE:])
    if s > minsize:
        minsize = s

    result = ["|"] * N
    level = 0
    next_level = 2
    for i in range(1, SEGTREE_SIZE):
        if i == next_level:
            level += 1
            next_level *= 2
        width = ((minsize + 1) << (N - 1 - level)) - 1
        result[level] += strs[i].center(width) + "|"
    print(*result, sep="\n")


def main():
    from operator import add
    N, Q = map(int, input().split())
    depth = N.bit_length() + 1
    set_depth(depth)
    table = [0] * SEGTREE_SIZE

    for time in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            s, t, value = args
            range_update(table, s, t + 1, lambda x: x + value)

        else:
            # find
            print(down_propagate_to_leaf(
                table, args[0], add, 0))


# tests
T1 = """
3 5
0 1 2 1
0 2 3 2
0 3 3 3
1 2
1 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    3
    5
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
