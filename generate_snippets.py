#!/usr/bin/env python3

import os
import json
snippets = {}


def push(prefix, desc, body=None):
    if not body:
        body = desc
        desc = prefix
    body = body.strip()
    if desc in snippets:
        print(f"{desc} already exists")
        desc = desc + "'"
    snippets[desc] = dict(
        scope="python",
        prefix=prefix,
        body=body.splitlines(),
        description=desc
    )


push("readlist", "read list of integers", """
list(map(int, input().split()))
""")

push("readints", "map(int, input().split())")

push("readanint", "read an integer", "int(input())")

push("profile", """
try:
    profile
except:
    def profile(f): return f
""")

push("line_profiler", """
kernprof -l $1.py && python3 -m line_profiler $1.py.lprof > ${2:prof}
""")

push("new", """
code $1.py && chmod +x $1.py
""")

push("test", """
./$1.py < in/$2 > output && diff output out/$2
""")

push("stest", """
./$1.py < input > output && diff output expect
""")

push("dp", """
dp("$1: $2", $2)
""")


push("init", """
#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
# INF = sys.maxsize
INF = 10 ** 10
# INF = float("inf")

def dp(*x):  # debugprint
    print(*x)

""")

push("main", """
def main():
    pass


def _test():
    import doctest
    doctest.testmod()

import sys
USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'void(i8,i8)')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    if (USE_NUMBA and sys.argv[-1] != '-p') or sys.argv[-1] == '--numba':
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import main  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        exit()
    elif len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline

    # read parameter
    A, B = map(int, input().split())
    main(A, B)
""")

path = os.path.join(os.path.dirname(__file__), ".vscode/snippet.code-snippets")
json.dump(snippets, open(path, "w"), indent=2)
