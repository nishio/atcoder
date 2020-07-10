"""
N=300
%timeit one_out_product(xs)
201 µs ± 1.57 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
%timeit one_out_product_fast(xs)
194 µs ± 1.36 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
%timeit bluteforce(xs)
27.2 ms ± 610 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

N=1000
%timeit one_out_product(xs)
737 µs ± 7.12 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit one_out_product_fast(xs)
707 µs ± 8.64 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit bluteforce(xs)
329 ms ± 5.11 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

N=3000
%timeit one_out_product(xs)
2.31 ms ± 34.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
%timeit one_out_product_fast(xs)
2.14 ms ± 55 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
%timeit bluteforce(xs)
2.98 s ± 18.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
"""
MOD = 10 ** 9 + 7


def one_out_product(xs):
    N = len(xs)
    head = [0] * (N + 1)
    cur = 1
    for i in range(N):
        cur *= xs[i]
        cur %= MOD
        head[i] = cur
    head[-1] = 1

    tail = [0] * (N + 1)
    cur = 1
    for i in range(N - 1, -1, -1):
        cur *= xs[i]
        cur %= MOD
        tail[i] = cur
    tail[-1] = 1

    ret = [head[i - 1] * tail[i + 1] % MOD for i in range(N)]
    return ret


def one_out_product_fast(xs):
    N = len(xs)
    ret = [1] * N
    prod = 1
    for i in range(N):
        ret[i] = prod
        prod *= xs[i]
        prod %= MOD
    prod = 1
    for i in range(N - 1, -1, -1):
        ret[i] *= prod
        ret[i] %= MOD
        prod *= xs[i]
        prod %= MOD
    return ret


def bluteforce(xs):
    N = len(xs)
    ret = [1] * N
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ret[i] *= xs[j]
            ret[i] %= MOD

    return ret


N = 3000
xs = range(1, N + 1)
a = one_out_product(xs)
b = one_out_product_fast(xs)
assert a == b
c = bluteforce(xs)
assert a == c
