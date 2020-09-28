import sys
N = 10
bit = [0] * (N + 1)  # 1-origin


def debug(*x):
    print(*x, file=sys.stderr)


def bit_add(pos, val):
    assert pos > 0
    x = pos
    while x <= N:
        debug(": x", x)
        bit[x] += val
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_sum(pos):
    assert pos > 0
    ret = 0
    x = pos
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


def bit_bisect(lower):  # not tested
    "find a s.t. v1 + v2 + ... + va >= lower"
    x = 0
    k = 1 << (N.bit_length() - 1)  # largest 2^m <= N
    while k > 0:
        if (x + k <= N and bit[x + k] < lower):
            lower -= bit[x + k]
            x += k
        k //= 2
    return x + 1


for i in range(N):
    bit_add(i + 1, 1)
    print(bit)
