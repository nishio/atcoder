# included from libs/factor.py
"""
O(N^{1/4}) Factorization
Derived from https://qiita.com/Kiri8128/items/eca965fe86ea5f4cbb98
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1:
            continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1:
                return 0
            t <<= 1
    return 1


def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        def f(x): return (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for _i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for _i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g):
                return g
            elif isPrimeMR(n // g):
                return n // g
            return findFactorRho(g)


def get_factors(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i*i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret

# end of libs/factor.py

# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    ret = []
    for i in range(1, N + 1):
        f = get_factors(i)
        x = sum(f.values()) + 1
        ret.append(x)
    print(*ret)

# tests
T1 = """
4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1 2 2 3
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