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


if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(sys.argv) == 1:
        # no option
        main()
    elif sys.argv[1] == "-t":
        _test()
    else:
        input = open(sys.argv[1]).buffer.readline
""")

push("numba", """
if sys.argv[-1] == 'ONLINE_JUDGE':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8,i8)')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    # read parameter
    A, B = map(int, input().split())
    from my_module import main
    print(main(A, B))
""")

path = os.path.join(os.path.dirname(__file__), ".vscode/snippet.code-snippets")
json.dump(snippets, open(path, "w"), indent=2)
