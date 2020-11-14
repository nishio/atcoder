debug_indent = 0


def debug(*x, msg=" "):
    import sys
    global debug_indent
    x = list(x)
    indent = 0
    if msg.startswith(">"):
        indent = 1
    if msg.startswith("<"):
        debug_indent -= 1
    msg = "  " * debug_indent + msg
    print(msg, *x, file=sys.stderr)
    debug_indent += indent


def debug_return_value(f):
    "decorator to print return value with dedent"
    def g(x):
        debug(x, msg="<")
        return x

    def fg(*args, **kw):
        return g(f(*args, **kw))

    return fg
