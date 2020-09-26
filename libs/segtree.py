"""
Segment Tree

Sample: ACL Beginner Contest D
def solve(N, K, AS):
    MAX_CAPACITY = 300_000
    set_width(MAX_CAPACITY + 10)

    count = [0] * SEGTREE_SIZE
    point_set(count, AS[0], 1, max)
    for i in range(1, N):
        A = AS[i]
        start = max(0, A - K)
        end = min(A + K + 1, MAX_CAPACITY + 1)
        best = range_reduce(count, start, end, max, -INF)
        point_set(count, A, best + 1, max)
    return range_reduce(count, 0, MAX_CAPACITY + 1, max, -INF)

"""


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
    assert right <= NONLEAF_SIZE
    ret_left = unity
    ret_right = unity
    # debug("left,right", left, right)
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


def get_value(table, pos):
    return table[NONLEAF_SIZE + pos]


def get_values(table, N=NONLEAF_SIZE):
    return table[NONLEAF_SIZE:NONLEAF_SIZE+N]

# --- end of library ---


INF = 10 ** 9 + 1


def solve(N, K, AS):
    MAX_CAPACITY = 300_000
    set_width(MAX_CAPACITY + 10)

    count = [0] * SEGTREE_SIZE
    point_set(count, AS[0], 1, max)
    for i in range(1, N):
        A = AS[i]
        start = max(0, A - K)
        end = min(A + K + 1, MAX_CAPACITY + 1)
        best = range_reduce(count, start, end, max, -INF)
        point_set(count, A, best + 1, max)
    return range_reduce(count, 0, MAX_CAPACITY + 1, max, -INF)


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


def debug(*x):
    import sys
    print(*x, file=sys.stderr)


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


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
