import numpy as np
N = 100
xs = np.zeros(N)
for i in range(N):
    s = np.random.randint(0, 20000 + 1, 26)
    s.sort()
    xs[i] = s[-1] - s[-2]

print(xs.mean(), xs.std())
