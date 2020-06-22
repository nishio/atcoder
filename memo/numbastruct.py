import sys
import numba


def foo(x):
    for k in x:
        print("k:", k)
        for a, b in x[k]:
            print(a, b)


if sys.argv[-1] == "-c":
    # numba compile
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export(
        'foo', 'void(DictType(int64,ListType(UniTuple(int64,2))))')(foo)
    cc.compile()
    exit()
else:
    x = numba.typed.Dict()
    x[1] = numba.typed.List([(1, 2), (3, 4)])
    x[100] = numba.typed.List([(100, 200)])

    if sys.argv[-1] == "-p":
        print(numba.typeof(x))
        # => DictType[int64,ListType[UniTuple(int64 x 2)]]
    else:
        from my_module import foo
        foo(x)
