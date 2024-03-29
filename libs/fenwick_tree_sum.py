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
    >>> ft.find_next(0)
    1
    >>> ft.find_next(1)
    4
    >>> ft.find_next(2)
    4
    """

    def __init__(self, size, value=0):
        self.size = size
        self.values = [0] * (size + 1)  # 1-origin
        self.raw_values = [0] * size  # for debug

        if value != 0:
            for i in range(1, size + 1):
                self.set(i, value)

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
        "find x s.t. sum(x) >= lower"
        x = 0
        k = 1 << (self.size.bit_length() - 1)  # largest 2^m <= N
        while k > 0:
            if (x + k <= self.size and self.values[x + k] < lower):
                lower -= self.values[x + k]
                x += k
            k //= 2
        return x + 1

    def find_next(self, pos):
        "for 0/1 data, find i s.t. i > pos and raw_values[i] == 1"
        s = self.sum(pos + 1) + 1
        return self.bisect(s) - 1

# --- end of library ---


def solve(N, Q, QS):
    values = list(range(1, N + 1))
    ft = FenwickTree(N)

    def swap(i):
        values[i], values[i + 1] = values[i + 1], values[i]
        if i > 0:
            ft.set(i - 1, 1)
        ft.set(i, 1)
        if i < N - 1:
            ft.set(i + 1, 1)

    for t, x, y in QS:
        if t == 1:
            x -= 1
            # swap query
            swap(x)
        else:
            x -= 1
            y -= 1
            # sort query
            s = ft.sum(x) + 1
            pos = ft.bisect(s) - 1
            while pos < y:
                ft.set(pos, 0)
                while pos >= x and values[pos] > values[pos + 1]:
                    swap(pos)
                    pos -= 1
                pos = ft.bisect(s) - 1

    return values


def main():
    # verified: PAST3N
    N, Q = map(int, input().split())
    QS = []
    for _i in range(Q):
        QS.append(tuple(map(int, input().split())))
    print(*solve(N, Q, QS))


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

T2 = """
10 15
1 3 0
1 5 0
1 4 0
1 2 0
1 3 0
2 4 7
1 5 0
1 7 0
1 9 0
1 8 0
2 3 5
1 8 0
1 9 0
1 5 0
1 2 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1 2 4 5 3 6 8 7 9 10
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
