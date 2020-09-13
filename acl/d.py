import numpy as np
N, M = map(int, input().split())
AS = np.array(list(map(int, input().split())), dtype=np.int64)
BS = np.array(list(map(int, input().split())), dtype=np.int64)
cs = np.convolve(AS, BS)
cs %= 998244353
print(*cs, sep=" ")
