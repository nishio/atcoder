# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def is_p(lr1, lr2):
    l1, r1 = lr1
    l2, r2 = lr2
    return (l1 <= r2 and l2 <= r1)


def aoki(LR):
    selected = []
    for lr1 in sorted(LR):
        if not any(is_p(lr1, lr2) for lr2 in selected):
            selected.append(lr1)
    return len(selected)


def takahashi(LR):
    from operator import itemgetter
    selected = []
    for lr1 in sorted(LR, key=itemgetter(1)):
        if not any(is_p(lr1, lr2) for lr2 in selected):
            selected.append(lr1)
    return len(selected)


def random_test():
    from random import seed, randint
    for s in range(1000_00):
        seed(s)
        LR = []
        for i in range(10):
            W = 999
            l = randint(0, W - 1)
            r = randint(l + 1, W)
            LR.append((l, r))
        t = takahashi(LR)
        a = aoki(LR)
        # if t != a:
        #     print(s, LR, t, a)
        if t - a > 8:
            print(s, LR, t, a)


"""
83 [(63, 93), (11, 28), (48, 51), (6, 90)] 3 1
"""


def solve(N, M):
    if M < 0:
        print(-1)
        return
    if M > N - 1:
        print(-1)
        return

    LR = []
    for i in range(M):
        LR.append((2 + i * 2, 3 + i * 2))
    end = 3 + 2 * (M - 1)

    rest = N - M - 1
    LR.append((1, end + 1 + rest))
    for i in range(rest):
        LR.append((end + 1 + i, end + 2 + rest + i))

    # assert (takahashi(LR) - aoki(LR)) == M
    # assert len(LR) == N
    for l, r in LR:
        print(l, r)


def main():
    # parse input
    N, M = map(int, input().split())
    solve(N, M)

# tests


def _test():
    random_test()
    # for i in range(100):
    #     solve(100, i)

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
