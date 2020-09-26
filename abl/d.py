#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve_0_WA(N, K, AS):
    candidates = [[0]]
    for i in range(1, N):
        A = AS[i]
        new_candidates = []
        for c in candidates:
            if abs(AS[c[-1]] - A) <= K:
                new_candidates.append(c[:])
                c.append(i)
                new_candidates.append(c)
                break
            else:
                new_candidates.append(c)
        else:
            new_candidates.append([i])
        candidates = new_candidates
        candidates.sort(key=len, reverse=True)
        debug("candidates", candidates)
    return len(candidates[0])


def set_depth(depth):
    global DEPTH, SEGTREE_SIZE, NONLEAF_SIZE
    DEPTH = depth
    SEGTREE_SIZE = 1 << DEPTH
    NONLEAF_SIZE = 1 << (DEPTH - 1)


def set_width(width):
    global WIDTH
    WIDTH = width
    set_depth((width - 1).bit_length() + 1)


def point_set(table, pos, value, binop):
    pos = pos + NONLEAF_SIZE
    table[pos] = value
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1],
        )


def range_reduce(table, left, right, binop, unity):
    ret_left = unity
    ret_right = unity
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
    while left < right:
        if left & 1:
            ret_left = binop(ret_left, table[left])
            left += 1
        if right & 1:
            right -= 1
            ret_right = binop(table[right], ret_right)

        left //= 2
        right //= 2
    return binop(ret_left, ret_right)


def bisect_left(table, left, right, value):
    left += NONLEAF_SIZE
    right += NONLEAF_SIZE
    left_left = None
    right_left = None
    while left < right:
        if left & 1:
            if left_left is None and table[left] >= value:
                left_left = left
            left += 1
        if right & 1:
            if table[right - 1] >= value:
                right_left = right - 1
        left >>= 1
        right >>= 1

    if left_left is not None:
        pos = left_left
        while pos < NONLEAF_SIZE:
            if table[2 * pos] >= value:
                pos = 2 * pos
            else:
                pos = 2 * pos + 1
        return pos - NONLEAF_SIZE
    elif right_left is not None:
        pos = right_left
        while pos < NONLEAF_SIZE:
            if table[2 * pos] >= value:
                pos = 2 * pos
            else:
                pos = 2 * pos + 1
        return pos - NONLEAF_SIZE
    else:
        return WIDTH


def full_up(table, binop):
    for i in range(NONLEAF_SIZE - 1, 0, -1):
        table[i] = binop(
            table[2 * i],
            table[2 * i + 1])


def solve(N, K, AS):
    count = [0] * 300_000
    count[AS[0]] = 1
    for i in range(1, N):
        A = AS[i]
        start = max(0, A - K)
        best = max(count[start:A + K + 1])
        count[A] = best + 1
    return max(count)


def solve(N, K, AS):
    set_width(300_010)

    table = [0] * SEGTREE_SIZE
    point_set(AS[0], 1)
    for i in range(1, N):
        A = AS[i]
        start = max(0, A - K)
        best = max(count[start:A + K + 1])
        count[A] = best + 1

    for _q in range(Q):
        q, x, y = map(int, input().split())
        if q == 1:
            # update
            point_set(table, x - 1, y, max)
        elif q == 2:
            # find
            print(range_reduce(table, x - 1, y, max, -INF))
        else:
            print(bisect_left(table, x - 1, N, y) + 1)


def main():
    # parse input
    N, K = map(int, input().split())
    AS = []
    for _i in range(N):
        AS.append(int(input()))

    print(solve(N, K, AS))


# tests
T1 = """
10 3
1
5
4
3
8
6
9
7
2
4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
7
"""

T2 = """
6 2
5
7
3
3
3
3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""

T3 = """
6 2
5
7
3
3
3
3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
5
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
