from collections import defaultdict
import sys
from math import gcd
count = defaultdict(int)
N = int(sys.stdin.readline())

zeros = 0
for i in range(N):
    A, B = [int(x) for x in input().split()]
    if A == B == 0:
        zeros += 1
        continue
    if A == 0:
        angle = (0, 1)
    elif B == 0:
        angle = (1, 0)
    else:
        sgn = A // abs(A)
        g = gcd(A, B)
        angle = (A // sgn // g, B // sgn // g)

    count[angle] += 1


# print(count)

pairs = {}
solos = []
for k1 in count:
    if k1 in pairs:
        continue
    if k1 == (0, 1):
        if (1, 0) in count:
            pairs[(1, 0)] = k1
        else:
            solos.append(k1)
        continue

    A, B = k1
    if B:
        sgn = -B // abs(B)
        k2 = (-B // sgn, A // sgn)
    else:
        k2 = (0, 1)
    if k2 in count:
        pairs[k2] = k1
    else:
        solos.append(k1)
#print(pairs, solos)

P = 1000000007


def pow2(n):
    # if n < 30:
    #     return 2 ** n

    # p = pow2(n // 2)
    # pp = (p * p) % P
    # if n % 2 == 1:
    #     return (2 * pp) % P
    # else:
    #     return pp
    return pow(2, n, P)


result = 1
for p in pairs:
    # print("pair", p, count[p], pairs[p], count[pairs[p]])
    n = count[p]
    m = count[pairs[p]]
    result = result * ((pow2(n) - 1) + (pow2(m) - 1) + 1) % P
for k in solos:
    # print("solo", k, count[k])
    result = result * pow2(count[k]) % P

print((result + zeros - 1) % P)
