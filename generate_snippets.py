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
INF = 10 ** 9 + 1
# INF = float("inf")

def dp(*x):  # debugprint
    print(*x)

""")

push("npreadints", """
${4:AB} = ${1:data}[:${2:2} * ${3:N}]
${1:data} = ${1:data}[${2:2} * ${3:N}:]
${4:AB} = ${4:AB}.reshape(-1, ${2:2})
for i in range(${3:N}):
    A, B = ${4:AB}[i]
""")

push("typedlist", """
${1:xs} = [${2:(0, 0)}]
${1:xs}.pop()
""")

push("main", """

def solve():
    passs
solve.signature = "void()"


def main():
    #N, Q = [int(x) for x in input().split()]
    #data = np.int64(read().split())
    #print(*solve(N, Q, data), sep="\\n")
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
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
    # cc.export('main', 'i8[:](i8,i8,i8[::1])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :], contiguous array[::1]
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
""")

path = os.path.join(os.path.dirname(__file__), ".vscode/snippet.code-snippets")
json.dump(snippets, open(path, "w"), indent=2)
