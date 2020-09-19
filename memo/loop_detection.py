"""
Loop Detection
ABC179 E
"""


def loop_detection(xs, N, M, DEBUG=False):
    """
    >>> loop_detection([3, 2, 1, 1], 5, 10, True) == sum([3, 2, 1, 1, 1])
    loop: [1]
    True

    >>> loop_detection([3, 2, 1, 2], 5, 10, True) == sum([3, 2, 1, 2, 1])
    loop: [2, 1]
    True

    >>> loop_detection([3, 2, 1, 3], 5, 10, True) == sum([3, 2, 1, 3, 2])
    loop: [3, 2, 1]
    True

    >>> loop_detection([3, 2, 1, 4, 5], 5, 10, True) == sum([3, 2, 1, 4, 5])
    no loop
    True
    """
    visited = [0] * M
    buffer = []
    for i, a in enumerate(xs):
        if visited[a]:
            sum_until_here = sum(buffer)
            loop_start = visited[a] - 1
            loop_end = i
            loop = buffer[loop_start:loop_end]
            loop_sum = sum(loop)
            loop_length = loop_end - loop_start
            loop_count = (N - i) // loop_length
            loop_remainder = (N - i) % loop_length
            sum_remainder = sum(loop[:loop_remainder])
            if DEBUG:
                print(f"loop: {loop}")
            return sum_until_here + loop_count * loop_sum + sum_remainder
        buffer.append(a)
        visited[a] = (i + 1)
    if DEBUG:
        print(f"no loop")
    return sum(buffer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
