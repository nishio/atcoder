"""
graveyard of snippets

put fresh one first
"""

# ----
push("readrest", "np.int64(read().split())")

push("npreadints", """
${4:AB} = ${1:data}[:${2:2} * ${3:N}]
${1:data} = ${1:data}[${2:2} * ${3:N}:]
${4:AB} = ${4:AB}.reshape(-1, ${2:2})
for i in range(${3:N}):
    A, B = ${4:AB}[i]
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

# ----
push("test", """
./$1.py < in/$2 > output && diff output out/$2
""")

push("stest", """
./$1.py < input > output && diff output expect
""")

push("typedlist", """
${1:xs} = [${2:(0, 0)}]
${1:xs}.pop()
""")
