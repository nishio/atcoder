import sys
import numpy as np


def solve():
    "void()"

    value = np.zeros(1, dtype=np.int32)
    value_pointer = 0

    def value_push(v):
        nonlocal value, value_pointer
        if value_pointer == value.size:
            # equivalent of `value.resize(value.size * 2)`
            old = value
            value = np.zeros(value.size * 2, dtype=value.dtype)
            value[:old.size] = old
            # ---
        value[value_pointer] = v
        value_pointer += 1

    next = np.zeros(1, dtype=np.int32)
    next_pointer = 0

    def next_push(v):
        nonlocal next, next_pointer
        if next_pointer == next.size:
            # equivalent of `next.resize(next.size * 2)`
            old = next
            next = np.zeros(next.size * 2, dtype=next.dtype)
            next[:old.size] = old
            # ---
        next[next_pointer] = v
        next_pointer += 1

    # use 0 as NULL
    value_push(0)
    next_push(0)

    K = 3
    head = np.zeros(K, dtype=np.int32)

    def push(i, v):
        p = value_pointer
        value_push(v)
        next_push(head[i])
        head[i] = p

    for i in range(10):
        push(i % 3, i)

    print(value)
    print(next)
    print(head)

    for i in range(3):
        cur = head[i]
        buf = []
        while cur != 0:
            buf.append(value[cur])
            cur = next[cur]
        print(i, buf)  # reversed inserted order


def main():
    solve()


def _test():
    import doctest
    doctest.testmod()


USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
    cc.compile()
    exit()
else:
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read

    if (USE_NUMBA and sys.argv[-1] != '-p') or sys.argv[-1] == "--numba":
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import solve  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
