"""
Fenwick Tree / Binary Indexed Tree (BIT)
for add/sum operation
"""


def bit_init(n, value=0):
    global N, bit, raw_value
    N = n
    bit = [value] * (N + 1)  # 1-origin
    raw_value = [value] * (N + 1)  # for debug


def bit_add(pos, val):  # point add / range sum
    assert pos > 0
    raw_value[pos] += val

    x = pos
    while x <= N:
        bit[x] += val
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_set(pos, val):
    bit_add(pos, val - raw_value[pos])


def bit_sum(pos):
    """
    sum for [0, pos)
    """
    ret = 0
    x = pos - 1
    while x > 0:
        ret += bit[x]
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

# --- end of library ---


def main():
    # verified: https://atcoder.jp/contests/practice2/tasks/practice2_b
    N, Q = map(int, input().split())
    bit_init(N)
    AS = list(map(int, input().split()))
    for i, a in enumerate(AS):
        bit_add(i + 1, a)

    for _q in range(Q):
        a, b, c = map(int, input().split())
        if a == 0:
            bit_add(b + 1, c)
        else:
            print(bit_sum(c) - bit_sum(b))


# tests
T1 = """
5 5
1 2 3 4 5
1 0 5
1 2 4
0 3 10
1 0 5
1 0 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
15
7
25
6
"""


# verified: https://atcoder.jp/contests/abc186/tasks/abc186_f

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
