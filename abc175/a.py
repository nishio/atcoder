def main():
    X = input().strip()
    if X == "RRR":
        return 3
    if "RR" in X:
        return 2
    if "R" in X:
        return 1
    return 0


print(main())
