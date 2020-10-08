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

# --- end of library ---


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
