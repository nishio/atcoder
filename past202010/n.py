# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(data):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353

    ZERO = ord("0")
    ONE = ord("1")
    QUEST = ord("?")

    table = [0] * (2 ** 12)
    table[0] = 1
    for y in range(18):
        for x in range(6):
            newtable = [0] * (2 ** 12)

            for s in range(2 ** 12):
                if table[s] == 0:
                    continue
                if data[y][x] == QUEST:
                    total = 0
                    if x > 0:
                        if (s >> (x - 1)) & 1:
                            total += 1
                        else:
                            total -= 1
                    else:
                        total -= 1

                    if x < 5:
                        if data[y][x + 1] == ONE:
                            total += 1
                        elif data[y][x + 1] == ZERO:
                            total -= 1
                    else:
                        total -= 1

                    up = (s >> x) & 1
                    if up:
                        total += 1
                    else:
                        total -= 1

                    debug(total, msg=":total")
                    if total != 3:
                        danger = (s >> (6 + x)) & 1
                        if not (up and danger):
                            # can place 0
                            next = s ^ (s & (1 << x))
                            if total == 1:
                                # danger, should not place 1 below
                                next |= (1 << 6)
                            debug(y, x, f"{s:06b}", f"{next:06b}",
                                  msg="canbe0:y, x")
                            newtable[next] += table[s]
                    if total != -3:
                        danger = (s >> (6 + x)) & 1
                        if not (not up and danger):
                            # can place 1
                            next = s | (1 << x)
                            if total == -1:
                                # danger, should not place 0 below
                                next |= (1 << 6)

                            debug(y, x, f"{s:06b}", f"{next:06b}",
                                  msg="canbe1:y, x")
                            newtable[next] += table[s]
                elif data[y][x] == ZERO:
                    next = s ^ (s & (1 << x))
                    newtable[next] += table[s]
                elif data[y][x] == ONE:
                    next = s | (1 << x)
                    newtable[next] += table[s]
                else:
                    raise RuntimeError

            table = newtable
            # debug(table, msg=":table")
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
_TEST_T4 = """
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
