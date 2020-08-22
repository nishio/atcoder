def readMap(H, W):
    global SENTINEL, HEIGHT, WIDTH
    SENTINEL = 2
    HEIGHT = H + SENTINEL * 2
    WIDTH = W + SENTINEL * 2
    data = [0] * (HEIGHT * WIDTH)
    ok = ord(".")
    for i in range(H):
        S = input().strip()
        y = (i + SENTINEL) * WIDTH
        for j in range(W):
            data[y + (j + SENTINEL)] = 1 if S[j] == ok else 0
    return data
