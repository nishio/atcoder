# included from snippets/main.py
from sys import dont_write_bytecode


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, X = map(int, input().split())
    AS = list(map(int, input().split()))
    from collections import defaultdict
    INF = 9223372036854775807
    table = defaultdict(lambda: -1)
    for k in range(1, 101):
        table[(0, k, 0)] = 0

    for a in AS:
        debug(table, msg=":table")
        for key in list(table):
            num, k, mod = key
            v = table[key] + a
            num += 1
            if num > k:
                continue
            mod = v % k

            key = (num, k, mod)
            table[key] = max(table[key], v)

    ret = INF
    for key in table:
        num, k, mod = key
        if num == k:
            if mod == X % k:
                s = (X - table[key]) // k
                debug(s, key, table[key], msg=":")
                ret = min(ret, s)

    print(ret)


# tests
T1 = """
3 9999999999
3 6 8
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4999999994
"""
T2 = """
1 1000000000000000000
1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
999999999999999999
"""
T3 = """
3 12
1 2 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2
"""
T4 = """
3 15
1 2 3
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3
"""
T6 = """
3 14
1 2 3
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
result
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
