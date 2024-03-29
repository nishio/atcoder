
# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_TLE(N, K):
    MOD = 1_000_000_007
    D = 2 ** 16
    less = [0] * D
    equal = 0
    for digit in N:
        digit = int(digit, 16)
        new_less = [0] * D
        less[0] += less[1]
        less[1] = 0
        for new_digit in range(16):
            bitmask = 2 ** new_digit
            for d in range(D):
                new_d = d | bitmask
                new_less[new_d] += less[d]

        for new_digit in range(16):
            if new_digit < digit:
                new_d = equal | (2 ** new_digit)
                new_less[new_d] += 1

        for d in range(D):
            new_less[d] %= MOD
        less = new_less
        equal = equal | (2 ** digit)

    ret = 0
    less[1] = 0  # it is 0
    less[equal] += 1
    for d in range(D):
        numBit = getNumBit(d)
        if numBit == K:
            ret += less[d]
    return ret % MOD

def solve(N, K):
    MOD = 1_000_000_007
    D = 16 + 1
    less = [0] * D
    equal_used = [0] * 16
    equal = 0
    for digit in N:
        digit = int(digit, 16)
        new_less = [0] * D
        for d in range(D):
            new_less[d] += less[d] * d

            if d == 0:
                new_less[d] += less[d] * 1
                new_less[d + 1] += less[d] * 15
            elif d != 16:
                new_less[d + 1] += less[d] * (16 - d)

        for new_digit in range(16):
            if new_digit < digit:
                new_d = equal
                if equal_used[new_digit] == 0:
                    new_d += 1
                if new_digit == 0 and equal == 0:
                    new_d = 0
                new_less[new_d] += 1

        for d in range(D):
            new_less[d] %= MOD
        less = new_less
        if equal_used[digit] == 0:
            equal += 1
            equal_used[digit] = 1
    ret = less[K]
    if equal == K:
        ret += 1
    return ret % MOD

def getNumBit(x):
    numBit = 0
    for i in range(16):
        numBit += x & 1
        x >>= 1
    return numBit

def main():
    N, K = input().strip().decode('ascii').split()
    K = int(K)
    print(solve(N, K))

# tests
T1 = """
10 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
15
"""
T2 = """
FF 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
225
"""
T3 = """
100 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
226
"""
T4 = """
1A8FD02 4
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3784674
"""
T5 = """
DEADBEEFDEADBEEEEEEEEF 16
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
153954073
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