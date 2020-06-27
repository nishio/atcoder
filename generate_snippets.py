#!/usr/bin/env python3

import os
import json
DIR = os.path.dirname(__file__)
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
debug("$1: $2", $2)
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

push("main", open(os.path.join(DIR, "snippets/main.py")).read())

path = os.path.join(DIR, ".vscode/snippet.code-snippets")
json.dump(snippets, open(path, "w"), indent=2)
