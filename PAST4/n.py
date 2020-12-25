# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(data):
    ZERO = ord("0")
    ONE = ord("1")

    onemasks = []
    zeromasks = []
    for y in range(18):
        onemask = 0
        zeromask = 0
        for i in range(6):
            if data[y][i] == ONE:
                onemask += 1 << i
            if data[y][i] != ZERO:
                zeromask += 1 << i
        onemasks.append(onemask)
        zeromasks.append(zeromask)

    def is_valid(y, s):
        return (
            onemasks[y] & s == onemasks[y] and
            zeromasks[y] | s == zeromasks[y]
        )

    def is_median(p1, p2, s):
        for i in range(6):
            # median check
            mask = (1 << i)
            neighbor = sum(
                x & mask > 0 for x in
                [p1, (p2 << 1), (p2 >> 1), s])
            is_ok_one = (p2 & mask) and neighbor >= 2
            is_ok_zero = not(p2 & mask) and neighbor <= 2
            if not (is_ok_one or is_ok_zero):
                return False
        return True

    def debugprint(*args):
        def to_s(x):
            return "".join(reversed(f"{x:06b}"))
        print(*[to_s(x) for x in args], sep="\n", file=sys.stderr)

    P6 = 2 ** 6
    P12 = 2 ** 12
    table = [0] * P12
    for s in range(P6):
        if is_valid(0, s):
            for s2 in range(P6):
                if is_valid(1, s) and is_median(0, s, s2):
                    table[s * P6 + s2] = 1

    for y in range(2, 18):
        newtable = [0] * P12
        for s in range(P6):
            if not is_valid(y, s):
                continue
            for past in range(P12):
                if table[past] == 0:
                    continue
                p1, p2 = divmod(past, P6)
                if is_median(p1, p2, s):
                    newtable[p2 * P6 + s] += table[past]
        table = newtable
    return sum(table)


def main():
    # parse input
    data = []
    for _i in range(18):
        data.append(input().strip())
    print(solve(data))


# tests
T1 = """
??0000
??0000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
???000
???000
???000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
000000
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
16
"""

T3 = """
?01000
1101?1
100111
1?11??
???00?
00011?
1?1??1
000101
100?11
1010??
?101??
?1??10
????10
?1??0?
1?1???
110?1?
0000?0
001?10
"""

TEST_T3 = """
>>> as_input(T3)
>>> main()
0
"""

T4 = """
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
??????
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
243882696958399859
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
