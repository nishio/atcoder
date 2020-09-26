#!/usr/bin/env python3
"""
generate snippets for VSCode
"""
import os
import json
DIR = os.path.dirname(__file__)
snippets = {}
snippets_for_global = {}


def push(prefix, desc, body=None, for_global=False):
    to_generate_desc = False
    if not body:
        body = desc
        to_generate_desc = True
    body = body.strip()
    lines = body.splitlines()

    if to_generate_desc:
        if lines[0] == '"""':
            desc = lines[1]
        else:
            desc = lines[0]

    if desc in snippets:
        print(f"{desc} already exists")
        desc = desc + "'"

    snip = dict(
        scope="python",
        prefix=prefix,
        body=lines,
        description=desc
    )
    if for_global:
        snippets_for_global[desc] = snip
    else:
        snippets[desc] = snip


push("readlist", "read list of integers", """
list(map(int, input().split()))
""")

push("readints", "map(int, input().split())")

push("readanint", "read an integer", "int(input())")

push("readstr",  "input().strip()")

push("readstrascii", "input().strip().decode('ascii')")

push("readquery", """
N, Q = map(int, input().split())
QS = []
for _q in range(Q):
    QS.append(tuple(map(int, input().split())))
""")

push("profile", "define @profile if not exist", """
try:
    profile
except:
    def profile(f): return f
""", for_global=True)

push("perf", "use perf_counter", """
start_time = perf_counter()
$CLIPBOARD
debug(f"$1: {(perf_counter() - start_time):.2f}")
""", for_global=True)

push("impperf", "perf_counter", "from time import perf_counter", for_global=True)

push("test", "define testcode", '''
T${1:} = """
$2
"""
TEST_T$1 = """
>>> as_input(T$1)
>>> main()
${3:result}
"""
''', for_global=True)

push("dp", "debug print", """
debug("$1", $1)
""")

push("bp", "conditional breakpoint", """
if ${1:True}:
    import pdb
    pdb.set_trace()
""", for_global=True)

push("cache", """
from functools import lru_cache
@lru_cache(maxsize=None)
""")


# import
push("impdef", "from collections import defaultdict")
push("impdeq", "from collections import deque")
push("impheap", "from heapq import heappush, heappop")
push("impnp", "import numpy as np")


push("deftest", """
def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)
""", for_global=True)

push("defdebug", """
def debug(*x):
    import sys
    print(*x, file=sys.stderr)
""", for_global=True)


push("ifmain", """
if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
""", for_global=True)

push("yesno", """
if $1:
    print("Yes")
else:
    print("No")
""")

push("as_input", """
def as_input(s):
    "use in test, use given string as input file"
    import io
    g = globals()
    f = io.StringIO(s.strip())

    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")
""")


def read_file(filename):
    data = open(os.path.join(DIR, filename)).read()
    if "# --- end of library ---" in data:
        data = data.split("# --- end of library ---")[0]
    return data


push("main", read_file("snippets/main.py"))
push("numbamain", read_file("snippets/numbamain.py"))
push("def_debug_indent", read_file("snippets/debug_indent.py"))
push("readmap", read_file("snippets/readMap.py"))

push("unionfind", read_file("libs/unionfind.py"))
push("segtree", read_file("libs/segtree.py"))
push("lazy_segtree", read_file("libs/lazy_segtree.py"))
push("dinic_maxflow", read_file("libs/dinic.py"))
push("loop_detection", read_file("libs/loop_detection.py"))
push("accum_dp", read_file("libs/accum_dp.py"))


def main():
    path = os.path.join(DIR, ".vscode/snippet.code-snippets")
    json.dump(snippets, open(path, "w"), indent=2)
    path = "/Users/nishio/Library/Application Support/Code/User/snippets/python.code-snippets"
    json.dump(snippets_for_global, open(path, "w"), indent=2)


if __name__ == "__main__":
    main()
