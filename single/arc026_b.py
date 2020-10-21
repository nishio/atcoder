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


def solve(N):
    s = sum(get_divisors(N))
    if s == 2 * N:
        return "Perfect"
    if s < 2 * N:
        return "Deficient"
    return "Abundant"


def main():
    N = int(input())
    print(solve(N))


# tests
T1 = """
6
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Perfect
"""

T2 = """
24
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
Abundant
"""

T3 = """
27
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Deficient
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
