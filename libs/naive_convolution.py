def convolution(xs, ys, MOD):
    ret = [0] * (len(xs) + len(ys) - 1)
    for i in range(len(xs)):
        for j in range(len(ys)):
            ret[i + j] += xs[i] * ys[j]
            ret[i + j] %= MOD
    return ret
