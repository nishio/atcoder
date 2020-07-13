import numpy as np

MOD = 10 ** 9 + 7

assert ((MOD - 1) ** 2).bit_length() == 60
N = 20
assert (N * (MOD - 1) ** 2).bit_length() == 65

x = np.array([MOD - 1] * N, dtype=np.int64)
assert x.dot(x) % MOD == 417656019  # incorrect answer

upper = x // (2 ** 15)
lower = x % (2 ** 15)
r30 = (2 ** 30) % MOD
r15 = (2 ** 15) % MOD
ret = (
    lower.dot(lower) % MOD +  # max: N * 2 ** 30
    lower.dot(upper) * 2 * r15 % MOD +  # max: N * 2 ** 46
    upper.dot(upper) * r30 % MOD  # max: N * 2 ** 57, safe??
) % MOD
assert ret == N  # correct answer

# minv = 1e+99
# i = 30000
# for i in range(30000, 60000_000):
#     v = (i * i) % MOD
#     if v < minv:
#         minv = v
#         print(i, v)

MOD = 10 ** 9 + 7
assert MOD.bit_length() == 30
SUBMOD = 31623
assert SUBMOD.bit_length() == 15
SUBMODSQ = 14122  # (SUBMOD ** 2) % MOD
assert SUBMODSQ.bit_length() == 14


def mat_mul_maspy(A, B):
    A1, A2 = A >> 15, A & (1 << 15) - 1
    B1, B2 = B >> 15, B & (1 << 15) - 1
    X = np.dot(A1, B1) % MOD
    Y = np.dot(A2, B2) % MOD
    Z = (np.dot(A1 + A2, B1 + B2) - X - Y) % MOD
    return ((X << 30) + (Z << 15) + Y) % MOD


def mat_mul_nishio(A, B):
    A1 = A // SUBMOD
    A2 = A % SUBMOD
    B1 = B // SUBMOD
    B2 = B % SUBMOD
    X = np.dot(A1, B1)  # 15 + 15 + log2(N) bit
    Y = np.dot(A2, B2)  # 15 + 15 + log2(N) bit
    Z = (np.dot(A1 + A2, B1 + B2) - X - Y)  # 16 + 16 + log2(N) bit
    return (X % MOD * SUBMODSQ + Z % MOD * SUBMOD + Y) % MOD


X = np.ones((2 ** 10, 2 ** 10), dtype=np.int64)
X *= MOD - 1

"""
In [329]: %timeit mat_mul_maspy(X, X)
7.5 s ± 306 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [330]: %timeit mat_mul_nishio(X, X)
7.93 s ± 391 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
"""
