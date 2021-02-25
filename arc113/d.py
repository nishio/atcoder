# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, K):
    MOD = 998_244_353
    if N == 1 or M == 1:
        return pow(K, N * M, MOD)
    if K == 2:
        N, M = min(N, M), max(N, M)
        ret = pow(2, (N + 1), MOD) + pow(2, M, MOD) - pow(2, N, MOD) - 1
        return ret % MOD
    1/0


def main():
    N, M, K = map(int, input().split())
    print(solve(N, M, K))

# tests


def foo(N, M, K):
    N, M = min(N, M), max(N, M)
    ret = pow(K, (N + 1)) + pow(K, M) - pow(K, N) - 1
    return ret


def blute(N, M, K):
    import itertools
    S = set()
    for xs in itertools.product(range(1, K + 1), repeat=N*M):
        r = (
            [min(xs[i * M: i * M + M]) for i in range(N)] +
            [max(xs[i:i + N * M:M]) for i in range(M)])
        S.add(tuple(r))

    # debug(sorted(S), msg=": S")
    return len(S)


# for i in range(1, 10):
#     assert blute(1, i, 2) == 2 ** i

# buf = []
# for i in range(1, 8):
#     # debug(i, blute(2, i, 3), msg=":i, blute(1, i, 2)")
#     debug(i, blute(3, i, 2), msg=":i, blute(1, i, 2)")
    # buf.append(blute(3, i, 2))


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
