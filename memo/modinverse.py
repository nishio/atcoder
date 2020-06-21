"""
Given K, N, R, find x s.t. Kx mod N = R
"""
R = 1234567

# Solve Kx + Ny = 1
N = 9999991
K = 2236206
a = N
b = K
vec = [(1, 0), (0, 1)]  # b = 0 N + 1 K
while True:
    q = a // b
    r = a % b
    # print(q, r)
    (aa, ab), (ba, bb) = vec
    vec = [(ba, bb), (aa - q * ba, ab - q * bb)]
    # print(vec)
    if r == 1:
        break
    a, b = b, r

_, (ba, bb) = vec
print(f"{N} * {ba} + {K} * {bb} == 1")
x = bb * R % N
print(f"{K} * {x} mod {N} = {R}")
