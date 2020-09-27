"""
Convolution
"""


# convolve
# derive from https://atcoder.jp/contests/practice2/submissions/16789717
MOD = 998244353
G = 3
InvG = 332748118  # mod_inverse(3, 998244353)
W = [pow(G, (MOD - 1) >> i, MOD) for i in range(24)]
iW = [pow(InvG, (MOD - 1) >> i, MOD) for i in range(24)]


def fft(k, f):
    for l in range(k, 0, -1):
        d = 1 << l - 1
        U = [1]
        for i in range(d):
            U.append(U[-1] * W[l] % MOD)

        for i in range(1 << k - l):
            for j in range(d):
                s = i * 2 * d + j
                fs = f[s]
                fsd = f[s + d]
                f[s] = (fs + fsd) % MOD
                f[s+d] = U[j] * (fs - fsd) % MOD


def ifft(k, f):
    for l in range(1, k + 1):
        d = 1 << l - 1
        for i in range(1 << k - l):
            u = 1
            for j in range(i * 2 * d, (i * 2 + 1) * d):
                f[j + d] *= u
                fj = f[j]
                fjd = f[j+d]
                f[j] = (fj + fjd) % MOD
                f[j+d] = (fj - fjd) % MOD
                u = u * iW[l] % MOD


def convolve(a, b):
    n0 = len(a) + len(b) - 1
    k = (n0).bit_length()
    n = 1 << k
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    fft(k, a)
    fft(k, b)
    for i in range(n):
        a[i] = a[i] * b[i] % MOD
    ifft(k, a)
    invn = pow(n, MOD - 2, MOD)
    for i in range(n0):
        a[i] = a[i] * invn % MOD
    del a[n0:]
    return a

# --- end of library ---


def debug(*x):
    print(*x, file=sys.stderr)


def solve(AS, BS):
    return convolve(AS, BS)


def main():
    # parse input
    N, M = map(int, input().split())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    print(*solve(AS, BS), sep=" ")


# tests
T1 = """
4 5
1 2 3 4
5 6 7 8 9
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5 16 34 60 70 70 59 36
"""

T2 = """
1 1
10000000
10000000
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
871938225
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
