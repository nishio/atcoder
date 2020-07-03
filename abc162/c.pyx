cdef gcd(int p, int q):
    cdef int r
    while q:
        r = p % q
        p = q
        q = r
    return p


def main():
    cdef int ans, i, j, l, K
    K = int(input())
    ans = 0

    for i in range(1, K+1):
        for j in range(1, K+1):
            for l in range(1, K+1):
                ans = ans + gcd(gcd(i, j), l)
    print(ans)


if __name__ == "__main__":
    main()
