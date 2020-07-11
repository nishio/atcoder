from itertools import accumulate, chain
XS = [1, 2, 3, 4, 5]
acc = list(chain([0], accumulate(XS)))
print(acc)  # => [0, 1, 3, 6, 10, 15]
assert acc[4] - acc[3] == XS[3]
assert acc[4] - acc[1] == sum(XS[1:4])
