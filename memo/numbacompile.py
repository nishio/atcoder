import numpy as np
import numba

from numba.pycc import CC
cc = CC('my_module')


@cc.export("bisect", "i8(i8[:], i8)")
def bisect(a, x):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    # if lo < 0:
    #     raise ValueError('lo must be non-negative')
    # if hi is None:
    #     hi = len(a)
    # FIXME: optional paramaters
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo


@cc.export("main", "i8(i8[:], i8)")
def main(xs, x):
    print(bisect(xs, x))


if 1:
    cc.compile()
else:
    from my_module import main

main(np.arange(10), 3)  # => 4
