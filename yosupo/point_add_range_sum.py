"""
Point Add Range Sum
"""
N, Q = [int(x) for x in input().split()]
AS = [int(x) for x in input().split()]

bit = [0] * 1000010  # 1-origin


def bit_add(pos, val):
    x = pos
    while x <= N:
        bit[x] += val
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_sum(pos):
    ret = 0
    x = pos
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


def bit_bisect(lower):
    "find a s.t. v1 + v2 + ... + va >= lower"
    x = 0
    k = 1 << (N.bit_length() - 1)  # largest 2^m <= N
    while k > 0:
        if (x + k <= N and bit[x + k] < lower):
            lower -= bit[x + k]
            x += k
        k //= 2
    return x + 1


for i, x in enumerate(AS):
    bit_add(i + 1, x)

for q in range(Q):
    typ, x, y = [int(x) for x in input().split()]
    if typ == 0:
        bit_add(x + 1, y)
    else:
        # print(bit[:6])
        # print(bit_sum(y))
        # print(bit_sum(x))
        print(bit_sum(y) - bit_sum(x))
