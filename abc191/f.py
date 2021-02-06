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

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    from math import gcd
    from functools import reduce
    N = int(input())
    AS = list(map(int, input().split()))
    minA = min(AS)
    S = set(AS)
    divisors = set()
    for x in S:
        divisors.update(get_divisors(x))
    ret = 1
    for d in sorted(divisors):
        if d == minA:
            break
        targets = [x for x in S if x % d == 0]
        if reduce(gcd, targets) == d:
            ret += 1
    print(ret)


# tests
T1 = """
3
6 9 12
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
4
8 2 12 6
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""

T3 = """
7
30 28 33 49 27 37 48
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
7
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
