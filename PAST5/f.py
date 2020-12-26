# included from libs/bin_to_str.py
def bin_to_str(x, digits=16):
    """
    >>> bin_to_str(10, 6)
    '001010'
    """
    format = "{x:0%db}" % digits
    return format.format(x=x)


def bin_to_revstr(x, digits=16):
    """
    >>> bin_to_revstr(10, 6)
    '010100'
    """
    return "".join(reversed(bin_to_str(x, digits)))


# end of libs/bin_to_str.py
# included from libs/sizeK_subsets.py
"""
all size K subsets of size N superset
"""


def all_sizeK_subsets(N, K):
    x = (1 << K) - 1
    FULL = 1 << N
    while x < FULL:
        yield x
        # example x = 00110110
        a = x & -x  # 00000010: rightmost one
        b = x + a   # 00111000
        c = x & ~b  # 00000110: rightmost one block
        d = c // a  # 00000011: remove trailing zeros
        e = d >> 1  # 00000001
        x = e | b   # 00111001

# end of libs/sizeK_subsets.py

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def _solve(N, rules):
    for K in range(N - 1, 0, -1):
        debug(K, msg=":K")
        for subset in all_sizeK_subsets(N, K):
            debug(subset, msg=":subset")
            for rs in rules:
                if all(subset & (1 << (r - 1)) for r in rs):
                    break
            else:
                return K
    return 0


def solve(N, rules):
    ret = 0
    for subset in range(2 ** N):
        danger = []
        for rs in rules:
            hit = 0
            for r in rs:
                if subset & (1 << (r - 1)):
                    hit += 1
                else:
                    d = r
            if hit == 3:
                danger = []
                break
            if hit == 2:
                danger.append(d)

        ret = max(ret, len(set(danger)))

    return ret


def main():
    # parse input
    N, M = map(int, input().split())
    rules = []
    for _i in range(M):
        rules.append(tuple(map(int, input().split())))
    print(solve(N, rules))


# tests
T1 = """
4 2
1 2 3
1 2 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
6 7
1 2 5
2 3 5
2 4 5
1 2 3
4 5 6
2 5 6
1 3 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
4
"""

T3 = """
5 1
1 2 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1
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
