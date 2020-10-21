# included from snippets/main.py

# included from libs/factor.py
"""
O(N^{1/4}) Factorization
Derived from https://qiita.com/Kiri8128/items/eca965fe86ea5f4cbb98
"""

# included from libs/divisor.py
"""
get all divisors
"""


def get_divisors(n, includeN=True):
    """
    >>> get_divisors(28)
    [1, 2, 4, 7, 14, 28]
    >>> get_divisors(28, includeN=False)
    [1, 2, 4, 7, 14]

    Derived from https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    upper_divisors = upper_divisors[::-1]
    if not includeN:
        upper_divisors.pop()
    return lower_divisors + upper_divisors


# end of libs/divisor.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353


def main():
    # parse input
    N = int(input())
    for x in get_divisors(N):
        print(x)
    # print(solve(SOLVE_PARAMS))


# tests
T = """
6
"""
TEST_T = """
>>> as_input(T)
>>> main()
1
2
3
6
"""

T2 = """
720
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
2
3
4
5
6
8
9
10
12
15
16
18
20
24
30
36
40
45
48
60
72
80
90
120
144
180
240
360
720
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
