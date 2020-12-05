from math import gcd
N = int(input())
x = 1
for i in range(2, N + 1):
    g = gcd(x, i)
    x *= i // g
print(x + 1)
