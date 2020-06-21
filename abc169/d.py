from math import sqrt
from collections import defaultdict
N = int(input())
factors = defaultdict(int)

upper = int(sqrt(N))
for p in range(2, upper + 1):
    while N % p == 0:
        factors[p] += 1
        N //= p
if N != 1:
    factors[N] = 1

# print(factors)
result = 0
for p in factors:
    fp = factors[p]
    ti = 1
    while True:
        # print(p, fp, ti)
        if fp >= ti:
            fp -= ti
            ti += 1
            result += 1
        else:
            break

print(result)
