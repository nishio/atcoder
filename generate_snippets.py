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

push("readrest", "np.int64(read().split())")

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

# push("test", """
# ./$1.py < in/$2 > output && diff output out/$2
# """)

# push("stest", """
# ./$1.py < input > output && diff output expect
# """)

push("npreadints", """
${4:AB} = ${1:data}[:${2:2} * ${3:N}]
${1:data} = ${1:data}[${2:2} * ${3:N}:]
${4:AB} = ${4:AB}.reshape(-1, ${2:2})
for i in range(${3:N}):
    A, B = ${4:AB}[i]
""")

# push("typedlist", """
# ${1:xs} = [${2:(0, 0)}]
# ${1:xs}.pop()
# """)

push("constant_append", """
${1:xs} = np.zeros(1, dtype=np.int32)
${1:xs}_pointer = 0

def ${1:xs}_push(v):
    nonlocal ${1:xs}, ${1:xs}_pointer
    if ${1:xs}_pointer == ${1:xs}.size:
        # equivalent of `${1:xs}.resize(${1:xs}.size * 2)`
        old = ${1:xs}
        ${1:xs} = np.zeros(${1:xs}.size * 2, dtype=${1:xs}.dtype)
        ${1:xs}[:old.size] = old
        # ---
    ${1:xs}[${1:xs}_pointer] = v
    ${1:xs}_pointer += 1
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

push("defdebugindent", """
debug_indent = 0
def debug(*x):
    import sys
    global debug_indent
    x = list(x)
    indent = 0
    if x[0].startswith("enter") or x[0][0] == ">":
        indent = 1
    if x[0].startswith("leave") or x[0][0] == "<":
        debug_indent -= 1
    x[0] = "  " * debug_indent + x[0]
    print(*x, file=sys.stderr)
    debug_indent += indent
""", for_global=True)

push("ifmain", """
if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
""", for_global=True)


def read_file(filename):
    data = open(os.path.join(DIR, filename)).read()
    if "# --- end of library ---" in data:
        data = data.split("# --- end of library ---")[0]
    return data


push("main", read_file("snippets/main.py"))
push("numbamain", read_file("snippets/numbamain.py"))
push("debug_indent", read_file("snippets/debug_indent.py"))
push("lazy_segtree", read_file("snippets/lazy_segtree.py"))
push("readmap", read_file("snippets/readMap.py"))
push("unionfind", read_file("libs/unionfind.py"))


def main():
    path = os.path.join(DIR, ".vscode/snippet.code-snippets")
    json.dump(snippets, open(path, "w"), indent=2)
    path = "/Users/nishio/Library/Application Support/Code/User/snippets/python.code-snippets"
    json.dump(snippets_for_global, open(path, "w"), indent=2)


if __name__ == "__main__":
    main()
