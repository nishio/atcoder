

# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N):
    P3 = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401, 10460353203, 31381059609, 94143178827, 282429536481, 847288609443,
          2541865828329, 7625597484987, 22876792454961, 68630377364883, 205891132094649, 617673396283947, 1853020188851841, 5559060566555523, 16677181699666569, 50031545098999707, 150094635296999121, 450283905890997363]
    P5 = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 30517578125, 152587890625, 762939453125,
          3814697265625, 19073486328125, 95367431640625, 476837158203125, 2384185791015625, 11920928955078125, 59604644775390625, 298023223876953125]
    for i, x in enumerate(P3):
        for j, y in enumerate(P5):
            if x + y == N:
                print(i + 1, j + 1)
                return
    print(-1)


def main():
    # parse input
    N = int(input())
    solve(N)


# tests
T1 = """
106
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4 2
"""

T2 = """
1024
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""

T3 = """
10460353208
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
21 1
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
