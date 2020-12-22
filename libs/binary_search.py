def binary_search_int(f, left=0, right=1000000):
    while left < right - 1:
        x = (left + right) // 2
        y = f(x)
        if y < 0:
            left = x
        else:
            right = x
    return right


def binary_search_float(f, left=0.0, right=1000000.0, eps=10**-7):
    while left < right - eps:
        x = (left + right) / 2
        y = f(x)
        if y < 0:
            left = x
        else:
            right = x
    return right
