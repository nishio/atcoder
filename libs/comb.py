"""
comb(N, K): O(K)
"""
MOD = 1_000_000_007


def comb_mod(n, k, MOD=MOD):
    assert n >= 0
    assert k >= 0
    if n < k:
        return 0
    k = min(k, n - k)
    a = 1
    b = 1
    for i in range(k):
        a *= (n - i)
        a %= MOD
        b *= (i + 1)
        b %= MOD
    return (a * mod_inverse(b, MOD)) % MOD


def comb(n, k):
    assert n >= 0
    assert k >= 0
    if n < k:
        return 0
    k = min(k, n - k)
    a = 1
    b = 1
    for i in range(k):
        a *= (n - i)
        b *= (i + 1)
    return a // b


# included from libs/mod_inverse.py
"""
Mod Inverse for single value
Given K, N, R, find x s.t. Kx mod N = R
"""


def mod_inverse(X, MOD):
    """
    return X^-1 mod MOD
    """
    return pow(X, MOD - 2, MOD)


# end of libs/mod_inverse.py

# --- end of library ---


def _test():
    MOD = 1_000_000_007
    N = 1000000000
    for i in range(1000):
        assert comb_mod(N, i, MOD) == comb(N, i) % MOD


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
    # main()
