# included from libs/fenwick_tree_sum.py
# included from libs/fenwick_tree_sum.py
"""
Fenwick Tree / Binary Indexed Tree (BIT)
for add/sum operation
* 0-origin interface
* raw values for debug
* instancible
"""


import sys


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


# end of libs/fenwick_tree_sum.py
#!/usr/bin/env python3
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, Q = map(int, input().split())
    CS = list(map(int, input().split()))

    QS = []
    for _q in range(Q):
        QS.append(tuple(map(int, input().split())))
    answer = {}

    ft = FenwickTree(N + 1)
    rightmost = [0] * (N + 1)
    current = 0
    for L, R in sorted(QS, key=(lambda x: x[1])):
        for i in range(current + 1, R + 1):
            c = CS[i - 1]
            ft.add(rightmost[c], -1)
            rightmost[c] = i
            ft.add(i, 1)
        current = R
        s = ft.sum(R + 1) - ft.sum(L)
        answer[(L, R)] = s

    for q in QS:
        print(answer[q])


# tests
T1 = """
4 3
1 2 1 3
1 3
2 4
3 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
3
1
"""

T2 = """
10 10
2 5 6 5 2 1 7 9 7 2
5 5
2 4
6 7
2 2
7 8
7 9
1 8
6 9
8 10
6 8
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
2
2
1
2
2
6
3
3
3
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


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
