"""
mprof run ...
mprof plot
"""

# x = set()
# for i in range(9_000_000):
#     x.add(i)

import numpy as np
x = np.zeros(9_000_000, np.bool_)
for i in range(9_000_000):
    x[i] = 1
