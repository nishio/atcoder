def main():
    X, N = [int(x) for x in input().split()]
    if N == 0:
        print(X)
        return

    PS = [int(x) for x in input().split()]
    for i in range(0, 100):
        for sign in (-1, +1):
            v = X + i * sign
            if v not in PS:
                print(v)
                return


main()
