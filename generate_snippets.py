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


def make_template(code, args):
    args = args.split()
    for i, arg in enumerate(args):
        placeholder = "${%d:%s}" % (i + 1, arg)
        code = code.replace(arg, placeholder)
    return code


push("readlist", "read list of integers", """
list(map(int, input().split()))
""")
push("readtuple", "tuple(map(int, input().split()))")

push("readints", "map(int, input().split())")

push("readanint", "read an integer", "int(input())")

push("readstr",  "input().strip()")

push("readstrascii", "input().strip().decode('ascii')")

push("readquery", """
N, Q = map(int, input().split())
# Q = int(input())
QS = []
for _q in range(Q):
    QS.append(tuple(map(int, input().split())))
""")

push("readtuples", make_template("""
XS = []
for _i in range(N):
    XS.append(tuple(map(int, input().split())))
""", "XS N"))

push("readedgecost", "read edges with cost", make_template("""
from collections import defaultdict
INF = 9223372036854775807
edges = defaultdict(lambda: defaultdict(lambda: INF))
for _i in range(NUM_EDGES):
    frm, to, cost = map(int, input().split())
    edges[frm-1][to-1] = cost  # -1 for 1-origin vertexes
    edges[to-1][frm-1] = cost  # if bidirectional
    # edges[frm-1][to-1] = min(edges[frm-1][to-1], cost)  # for multiple edges 
""", "NUM_EDGES -1"))

push("readedges", "read costless edges", make_template("""
from collections import defaultdict
edges = defaultdict(list)
for _i in range(NUM_EDGES):
    frm, to = map(int, input().split())
    edges[frm-1].append(to-1)  # -1 for 1-origin vertexes
    edges[to-1].append(frm-1)  # if bidirectional
""", "NUM_EDGES -1"))

push("readbigint", "[x - ord('0') for x in input().strip()]")
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

push("dpold", "debug print", """
debug("$1", $1)
""", for_global=True)

push("dp", "debug print", """
debug($1, msg="$2:$1")
""", for_global=True)

push("bp", "conditional breakpoint", """
if ${1:True}:
    import pdb
    pdb.set_trace()
""", for_global=True)

push("cache", """
from functools import lru_cache
@lru_cache(maxsize=None)
""", for_global=True)


push("unpack", make_template("""
x = pair >> 32
y = pair - (x << 32)
""", "pair 32 x y"))

push("pack", make_template("""
pair = (x << 32) + y
""", "pair 32 x y"))

# import
push("impdef", "from collections import defaultdict", for_global=True)
push("impcou", "from collections import Counter", for_global=True)
push("impdeq", "from collections import deque", for_global=True)
push("impheap", "from heapq import heappush, heappop", for_global=True)
push("impnp", "import numpy as np", for_global=True)


push("deftest", """
def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)
""", for_global=True)

push("defdebug", """
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)
""", for_global=True)


push("ifmain", """
if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
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

push("MOD1", "MOD = 1_000_000_007")
push("MOD9", "MOD = 998_244_353")
push("INF", "INF = 9223372036854775807")

push("for_subset", make_template("""
for subset in range(2 ** N):
    for i in range(N):
        if subset & (1 << i):
            pass
    pass
""", "subset N i"))

push("use_mincostflow", """
global mcf
mcf = MinCostFlow(numVertex)
# construct graph
mcf.add_edge(frm, to, capacity, cost)
# debug
print(list(mcf.edges()))
# flow
cap, cost = mcf.flow(start, goal)
""")

EOL = "# --- end of library ---"
push("eol", "end of library", EOL)


def read_file(filename):
    data = open(os.path.join(DIR, filename)).read()
    if EOL in data:
        data = data.split(EOL)[0]
    data = data.strip() + "\n"
    return f"# included from {filename}\n{data}\n# end of {filename}"


push("main", read_file("snippets/main.py"))
push("numbamain", read_file("snippets/numbamain.py"))
push("def_debug_indent", read_file("snippets/debug_indent.py"))

# register libs/*.py
for filename in os.listdir(os.path.join(DIR, "libs")):
    if filename.endswith(".py"):
        prefix = filename.replace(".py", "")
        push(prefix, read_file(os.path.join("libs", filename)))


def main():
    path = os.path.join(DIR, ".vscode/snippet.code-snippets")
    json.dump(snippets, open(path, "w"), indent=2)
    path = "/Users/nishio/Library/Application Support/Code/User/snippets/python.code-snippets"
    json.dump(snippets_for_global, open(path, "w"), indent=2)


if __name__ == "__main__":
    main()
