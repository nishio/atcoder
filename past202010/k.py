# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


# included from libs/fenwick_tree.py
"""
Fenwick Tree / Binary Indexed Tree (BIT)
"""


def init(n, value=0):
    global N, bit
    N = n
    bit = [value] * (N + 1)  # 1-origin


def bit_add(pos, val):  # point add / range sum
    assert pos > 0
    x = pos
    while x <= N:
        bit[x] += val
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_set(pos, val):  # point set / range max
    assert pos > 0
    x = pos
    while x <= N:
        bit[x] = max(bit[x], val)
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_point_action(pos, action_force, action):  # not tested
    assert pos > 0
    x = pos
    while x <= N:
        bit[x] = action_force(bit[x], action)
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_max(pos):
    assert pos > 0
    ret = 0
    x = pos
    while x > 0:
        ret = max(ret, bit[x])
        x -= x & -x
    return ret


def bit_sum(pos):
    ret = 0
    x = pos
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


def bit_range_reduce(pos, value_binop, value_unity):  # not tested
    ret = value_unity
    x = pos
    while x > 0:
        ret = value_binop(ret, bit[x])
        x -= x & -x
    return ret


def bit_bisect(lower):
    "find a s.t. v1 + v2 + ... + va >= lower"
    x = 0
    k = 1 << (N.bit_length() - 1)  # largest 2^m <= N
    while k > 0:
        if (x + k <= N and bit[x + k] < lower):
            lower -= bit[x + k]
            x += k
        k //= 2
    return x + 1


# end of libs/fenwick_tree.py
def solve(K, seqs, Q, BS):
    MOD = 10 ** 9
    N = 20
    bit = [0] * (N + 1)  # 1-origin

    n = 0
    ret = 0
    for b in BS:
        for a in seqs[b - 1]:
            s = 0
            x = a
            while x > 0:
                s += bit[x]
                x -= x & -x

            ret += (n - s)

            n += 1

            x = a
            while x <= N:
                bit[x] += 1
                x += x & -x  # (x & -x) = rightmost 1 = block width

            ret %= MOD
    return ret


def main():
    # parse input
    K = int(input())
    seqs = []
    for _i in range(K):
        _n = int(input())
        seqs.append(list(map(int, input().split())))
    Q = int(input())
    BS = list(map(int, input().split()))
    print(solve(K, seqs, Q, BS))


# tests
T1 = """
2
3
1 3 2
2
5 4
2
1 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
10
8
16 6 15 10 18 13 17 11
13
4 10 6 4 14 17 13 9 3 9 4 8 14
11
11 17 12 3 13 8 10 11 18 2 19
10
18 11 16 19 4 17 7 3 5 8
3
3 10 9
13
8 17 20 8 20 1 5 17 4 16 18 20 4
15
11 2 1 16 8 17 4 7 3 6 4 13 16 16 16
2
12 12
8
7 14 7 5 8 17 19 4
15
3 6 1 16 11 5 3 15 9 15 12 15 5 19 7
20
4 3 7 6 1 8 2 3 9 8 6 3 10 9 7 7 3 2 2 10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
12430
"""

T3 = """
1
3
1 2 3
1
1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
"""

T4 = """
1
3
3 2 1
1
1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3
"""

T5 = """
1
3
3 3 1
1
1
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
2
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


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
