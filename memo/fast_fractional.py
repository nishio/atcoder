

# Fast Fractional
"""
from collections import defaultdict
from math import gcd
zeros = 0
count = defaultdict(int)
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
"""
