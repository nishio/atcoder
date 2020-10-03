# included from snippets/main.py
def debug(*x):
    import sys
    print(*x, file=sys.stderr)


def solve(N, AB):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353

    used = [0] * (2 * N + 10)
    fixed = []
    tofix_a = []
    tofix_b = []
    tofix_both = 0
    for a, b in AB:
        if a != -1:
            if used[a] != 0:
                return "No"
            used[a] = 1
            if b != -1:
                if b < a:
                    return "No"
                fixed.append((a, b))
                used[b] = 1
            else:
                tofix_b.append(a)
        else:
            if b != -1:
                if used[b] != 0:
                    return "No"
                used[b] = 1
                tofix_a.append(b)
            else:
                tofix_both += 1

    diff = [0] * (2 * N + 10)

    def paint(a, b):
        """
        return True when failed
        """
        d = b - a
        for i in range(a, b + 1):
            if diff[i] != 0 and diff[i] != d:
                return True
            diff[i] = d
        return False

    for a, b in fixed:
        # debug("a, b", a, b)
        if paint(a, b):
            return "No"

    # debug("tofix_a", tofix_a)
    # debug("tofix_b", tofix_b)

    def fix_both(i):
        if i == tofix_both:
            return False  # success

        copy_diff = diff[:]
        for a in range(1, 2 * N):
            if used[a]:
                continue
            if diff[a] != 0:
                if a + diff[a] >= 2 * N + 1:
                    continue
                bs = [a + diff[a]]
            else:
                bs = range(a + 1, 2 * N + 1)

            for b in bs:
                # debug("a, b", a, b)
                if used[b]:
                    continue
                if diff[b] != 0 and b - diff[b] != a:
                    continue
                r = paint(a, b)
                if r:
                    diff[:] = copy_diff
                    continue
                r = fix_both(i + 1)
                if r:
                    diff[:] = copy_diff
                    continue
                return False
        return True

    def fix_a(i):
        # debug("fix a",  i)
        if i == len(tofix_a):
            return fix_both(0)

        b = tofix_a[i]
        if diff[b] != 0:
            a = b - diff[b]
            if used[a]:
                return True
            if paint(a, b):
                return True
            return fix_a(i + 1)
        else:
            copy_diff = diff[:]
            for a in range(1, b):
                if used[a]:
                    continue
                if diff[a] != 0 and b - diff[b] != a:
                    continue
                r = paint(a, b)
                if r:
                    diff[:] = copy_diff
                    continue
                r = fix_a(i + 1)
                if r:
                    diff[:] = copy_diff
                    continue
                return False
            return True

    def fix_b(i):
        # debug("fix b", i)
        if i == len(tofix_b):
            return fix_a(0)

        a = tofix_b[i]
        # debug("a", a)
        if diff[a] != 0:
            b = a + diff[a]
            if used[b]:
                return True
            if paint(a, b):
                return True
            # debug("single b fixed", b)
            return fix_b(i + 1)
        else:
            copy_diff = diff[:]
            for b in range(a + 1, 2 * N + 1):
                # debug("b", b)
                if used[b]:
                    # debug("b used", b)
                    continue
                if diff[b] != 0 and a + diff[b] != b:
                    # debug("b bad diff", b)
                    continue
                r = paint(a, b)
                if r:
                    diff[:] = copy_diff
                    continue
                # debug("single b temp fix", b)
                r = fix_b(i + 1)
                if r:
                    # debug("recover", b)
                    diff[:] = copy_diff
                    continue
                # debug("success")
                return False
            # debug("fail")
            return True

    # debug("fix_b")
    # debug("tofix_a, tofix_b", tofix_a, tofix_b)
    # debug("tofix_both", tofix_both)
    if fix_b(0):
        return "No"
    else:
        return "Yes"


def main():
    # parse input
    N = int(input())
    AB = []
    for _i in range(N):
        AB.append(tuple(map(int, input().split())))
    print(solve(N, AB))


# tests
T1 = """
3
1 -1
-1 4
-1 6
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
2
1 4
2 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
"""

T3 = """
2
4 1
2 4
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
No
"""

T4 = """
3
1 -1
-1 2
-1 6
"""
_TEST_T4 = """
>>> as_input(T4)
>>> main()
No
"""

T5 = """
3
1 2
3 4
5 6
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
Yes
"""

T6 = """
3
1 6
-1 -1
-1 -1
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
No
"""

T7 = """
3
1 2
1 -1
-1 -1
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
No
"""

T8 = """
3
1 2
2 -1
-1 -1
"""
TEST_T8 = """
>>> as_input(T8)
>>> main()
No
"""


def random_test():
    import numpy as np
    for i in range(10000):
        np.random.seed(i)
        N = np.random.randint(1, 100)
        solve(N, np.random.randint(1, 2 * N, (N, 2)))


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
