from numba.pycc import CC


def main():
    ds = {1: (2, 3)}       # (A)
    x = ds.get(1, (4, 5))  # (B)
    # x = ds[1]            # (B2)
    y = x[1]               # (C)


cc = CC('my_module')
cc.export('main', '()')(main)
cc.compile()
