class PowTable:
    def __init__(self, n, max_value, mod):
        xs = [1]
        for i in range(max_value):
            xs.append(xs[-1] * n % mod)
        self.table = xs

    def pow(self, k):
        return self.table[k]