buf = [1, 2]
for i in range(20000):
    n = (buf[-1] * 2) % 1000000007
    if n in buf:
        print(buf, n)
        break
    buf.append(n)
print(buf)
