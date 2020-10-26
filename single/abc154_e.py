# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, K):
    less = [0] * (K + 2)
    equal = 0
    for v in N:
        new_less = [0] * (K + 2)
        if v != 0 and equal <= K:
            new_less[equal] += 1  # for 0
            new_less[equal + 1] += v - 1  # for 1..
            equal += 1

        for k in range(K + 1):
            new_less[k] += less[k]  # for 0
            new_less[k + 1] += 9 * less[k]  # for 1..9
        less = new_less

    ret = less[K]
    if equal == K:
        ret += 1
    return ret


def main():
    # parse input
    N = [x - ord("0") for x in input().strip()]
    K = int(input())
    print(solve(N, K))


# tests
T1 = """
100
1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
19
"""

T2 = """
25
2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
14
"""

T3 = """
314159
2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
937
"""
T4 = """
9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
3
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
117879300
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
