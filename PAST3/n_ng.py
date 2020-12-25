# included from libs/fenwick_tree_sum.py
"""
Fenwick Tree / Binary Indexed Tree (BIT)
for add/sum operation
* 0-origin interface
* raw values for debug
* instancible
"""


class FenwickTree:
    """
    >>> ft = FenwickTree(10)
    >>> ft.add(1, 1)
    >>> ft.add(4, 2)
    >>> ft.add(7, 4)
    >>> ft.raw_values
    [0, 1, 0, 0, 2, 0, 0, 4, 0, 0]
    >>> [ft.sum(i) for i in range(10)]
    [0, 0, 1, 1, 1, 3, 3, 3, 7, 7]
    >>> ft.bisect(3)
    5
    """

    def __init__(self, size, value=0):
        self.size = size
        self.values = [value] * (size + 1)  # 1-origin
        self.raw_values = [value] * size  # for debug

    def add(self, pos, val):
        self.raw_values[pos] += val

        x = pos + 1
        while x <= self.size:
            self.values[x] += val
            x += x & -x  # (x & -x) = rightmost 1 = block width

    def set(self, pos, val):
        self.add(pos, val - self.raw_values[pos])

    def sum(self, pos):
        """
        sum for [1, pos)
        """
        ret = 0
        x = pos
        while x > 0:
            ret += self.values[x]
            x -= x & -x
        return ret

    def bisect(self, lower):
        "find a s.t. v1 + v2 + ... + va >= lower"
        x = 0
        k = 1 << (self.size.bit_length() - 1)  # largest 2^m <= N
        while k > 0:
            if (x + k <= self.size and self.values[x + k] < lower):
                lower -= self.values[x + k]
                x += k
            k //= 2
        return x + 1


# end of libs/fenwick_tree_sum.py
# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, Q, QS):
    ft = FenwickTree(N)
    ft.set(0, 1)
    start = [None] * N
    end = [None] * N
    start[0] = 0
    end[0] = N

    for t, x, y in QS:
        if t == 1:
            # swap query
            s = ft.sum(x)
            pos = ft.bisect(s)
            s = start[pos]
            e = end[pos]
            width = e - s
            if x == pos:
                start[pos] =
                pass
            elif x + 1 == pos + width:
                pass


def main():
    # parse input
    N, Q = map(int, input().split())
    QS = []
    for _i in range(Q):
        QS.append(tuple(map(int, input().split())))
    print(solve(N, Q, QS))


# tests
T1 = """
5 3
1 1 0
1 2 0
2 2 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2 1 3 4 5
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
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
    sys.setrecursionlimit(10 ** 6)
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py
