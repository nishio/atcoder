TINY_TEST = False

if TINY_TEST:
    MIN_BOUND = -2
    MAX_BOUND = 2
else:
    MIN_BOUND = -200
    MAX_BOUND = 200

WIDTH = (MAX_BOUND - MIN_BOUND) + 3
M = [["."] * WIDTH for i in range(WIDTH)]


def set(p, v):
    x, y = p
    M[y - MIN_BOUND + 1][x - MIN_BOUND + 1] = v


def get(p):
    x, y = p
    return M[y - MIN_BOUND + 1][x - MIN_BOUND + 1]


START = (0, 0)
if TINY_TEST:
    GOAL = (2, 2)

    set(START, "S")
    set(GOAL, "G")
    obstacles = [(1, 1)]
    for p in obstacles:
        set(p, "#")
else:
    N, X, Y = [int(x) for x in input().split()]
    set((X, Y), "G")
    for i in range(N):
        p = [int(x) for x in input().split()]
        set(p, "#")


def pp(map):
    for line in map:
        print("".join(line))


def main():

    def visit(x, y):
        if get((x, y)) == "G":
            return True
        if get((x, y)) != ".":
            return
        if x < MIN_BOUND-1 or MAX_BOUND+1 < x:
            return
        if y < MIN_BOUND-1 or MAX_BOUND+1 < y:
            return
        newFront.append((x, y))

    newFront = [START]
    for numSteps in range(1, 1000):
        front = newFront
        newFront = []
        for x, y in front:
            isFinished = (
                visit(x + 1, y + 1)
                or visit(x, y + 1)
                or visit(x - 1, y + 1)
                or visit(x + 1, y)
                or visit(x - 1, y)
                or visit(x, y - 1))
            if isFinished:
                print(numSteps)
                return
        if not newFront:
            print(-1)
            return


main()
