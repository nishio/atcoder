def foo(xs, i):
    if i < 0: return 0
    return foo(xs, i - 1) + xs[i]

print(foo([1,2,3,4,5,6,7], 6))
