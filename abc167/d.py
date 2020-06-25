import sys
import numpy as np


def solve(N, K, xs):
    "void()"
    town_to_time = np.zeros(N, np.uint32)
    time_to_town = np.zeros(N, np.uint32)
    cur = 1
    for i in range(K):
        cur = xs[cur - 1]
        # print(town_to_time, time_to_town, cur)
        if town_to_time[cur - 1]:
            # visited before
            period = i + 1 - town_to_time[cur - 1]
            rest = K - i - 1
            rest %= period
            # print(rest, town_to_time[cur - 1], town_to_time[cur - 1] + rest)
            print(time_to_town[town_to_time[cur - 1] + rest - 1])
            return

        town_to_time[cur - 1] = i + 1
        time_to_town[i] = cur
    print(cur)


IN1 = """
4 5
3 2 4 1
"""

IN2 = """
6 727202214173249351
6 5 2 5 3 2
"""

IN3 = """
6 100
2 3 4 5 6 1
"""


def main():
    """
    >>> as_input(IN1)
    >>> main()
    4
    >>> as_input(IN2)
    >>> main()
    2
    >>> as_input(IN3)
    >>> main()
    5
    """
    N, K = map(int, input().split())
    xs = np.array(list(map(int, input().split())))
    solve(N, K, xs)


def _test():
    import doctest
    as_input(IN1)
    main()
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())
    input = f.readline
    read = f.read


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
