
# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, K):
    MOD = 1_000_000_007
    D = 2 ** 16
    less = [0] * D
    equal = 0
    for digit in N:
        digit = int(digit, 16)
        new_less = [0] * D
        for new_digit in range(16):
            for d in range(D):
                if d == 1:  # zero only
                    new_d = (2 ** new_digit)
                else:
                    new_d = d | (2 ** new_digit)
                new_less[new_d] += less[d]
            if new_digit < digit:
                new_d = equal | (2 ** new_digit)
                new_less[new_d] += 1
        for d in range(D):
            new_less[d] %= MOD
        less = new_less
        equal = equal | (2 ** digit)
        # x = [i for i in range(D) if less[i]]
        # debug(x, msg=":debug")
        # debug(equal, msg=":equal")
    ret = 0
    less[1] = 0  # it is 0
    less[equal] += 1
    for d in range(D):
        numBit = getNumBit(d)
        if numBit == K:
            ret += less[d]
            # debug(d, less[d], msg=":d, less[d]")
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