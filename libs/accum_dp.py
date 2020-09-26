"""
DP with accumulation
ABC179 D
"""


def dp_with_accum(N, K, SS):
    count = [0] * (N + 10)
    accum = [0] * (N + 10)

    # initial value
    accum[0] = count[0] = 1
    MOD = 998244353

    for pos in range(1, N):
        # calc new value
        next_value = 0
        for left, right in SS:
            start = pos - right
            end = pos - left
            next_value += (accum[end] - accum[start - 1])
            next_value %= MOD

        count[pos] = next_value
        accum[pos] = accum[pos - 1] + next_value

    # return last value
    ret = count[N - 1]
    return ret % MOD

# --- end of library ---


def main():
    # parse input
    N, K = map(int, input().split())
    SS = []
    for _i in range(K):
        SS.append(tuple(map(int, input().split())))
    print(dp_with_accum(N, K, SS))


# tests
T1 = """
5 2
1 1
3 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
5 2
3 3
5 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
5 1
1 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
5
"""

T4 = """
60 3
5 8
1 3
10 15
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
221823067
"""

T5 = """
10 1
1 2
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
55
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
