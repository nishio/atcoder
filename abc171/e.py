from functools import reduce
from operator import xor

N = int(input())
AS = list(map(int, input().split()))
if N == 2:
    print(*AS, sep=" ")
    exit()
if N == 3:
    r0 = 0
    r1 = r0 ^ AS[2]
    r2 = r1 ^ AS[0]
    print(r0, r1, r2)
    exit()

"""
input
0b00000000000000000000000010100
0b00000000000000000000000001011
0b00000000000000000000000001001
0b00000000000000000000000011000

output
0b00000000000000000000000011010
0b00000000000000000000000000101
0b00000000000000000000000000111
0b00000000000000000000000010110

myanswer
0b00000000000000000000000000000
0b00000000000000000000000011111
0b00000000000000000000000011101
0b00000000000000000000000001100
"""
# for a in AS:
#     print(f"{a:#031b}")
r = [0] * N
for i in range(1, N):
    r[i] = r[i - 1] ^ AS[i - 1] ^ AS[i]

# for a in r:
#     print(f"{a:#031b}")

rest = reduce(xor, r[1:])
d = AS[0] ^ rest
for i in range(N):
    r[i] ^= d

print(*r)
# check
# total = reduce(xor, r)
# for i in range(N):
#     print(total ^ r[i] == AS[i])
