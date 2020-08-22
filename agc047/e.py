CODE = """
< 3 0 4
< 3 1 5
+ 4 5 6
< 3 6 7
< 7 6 8
"""

"""
< 9 0 13 
< 12 1 14
+ 13 14 15
< 7 15 15
+ 2 15 2

"""

memory = [0] * 20
memory[0] = 7
memory[1] = 9
for line in CODE.strip().split("\n"):
    cmd, i, j, k = line.split()
    i = int(i)
    j = int(j)
    k = int(k)
    if cmd == "+":
        memory[k] = memory[i] + memory[j]
    elif cmd == "<":
        memory[k] = 1 if memory[i] < memory[j] else 0
    print(memory)
