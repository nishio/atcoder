from functools import reduce
from operator import xor

N = int(input())
AS = list(map(int, input().split()))
total = reduce(xor, AS)
print(*[a ^ total for a in AS])
