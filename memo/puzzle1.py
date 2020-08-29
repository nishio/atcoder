GAME = """
 1#  3#3 
2# 1 #2  
  3#3  #1
   1#    
# # 3 # #
    #1   
4#  1#2  
  2# 4 #1
 2#1  #3 
"""
GAME = """
41#2 3#3 
2# 1 #21 
  3#3  #1
   1#    
# # 3 # #
    #1   
4#  1#2  
 42# 4 #1
12#1 3#3 
"""
GAME = """
41#243#34
2#412#213
123#324#1
3421#3142
#1#234#3#
2314#1423
4#431#214
342#341#1
12#143#32
"""

GAME = GAME.strip("\n").split("\n")
N = 9
data = ["#" * 11] + [f"#{line}#" for line in GAME] + ["#" * 11]
print(data)
rs = [None, {}, {}, {}, {}]
for y in range(10):
    for x in range(10):
        if data[y][x] == "#":
            buf = []
            dx = 1
            while data[y][x + dx] != "#":
                assert data[y][x + dx] not in [x for x in buf if x != " "]
                buf.append(data[y][x + dx])
                dx += 1
            if buf:
                rs[len(buf)][(x + 1, y, "x")] = buf

            buf = []
            dy = 1
            while data[y + dy][x] != "#":
                assert data[y + dy][x] not in [x for x in buf if x != " "]
                buf.append(data[y + dy][x])
                dy += 1
            if buf:
                rs[len(buf)][(x, y + 1, "y")] = buf

# for k in sorted(rs[2]):
#     print(rs[2][k], k)

for a in "1234":
    for k in sorted(rs[3]):
        v = rs[3][k]
        if v[2] == a:
            print(v, k)
    print()

# for a in "1234":
#     for k in sorted(rs[4]):
#         v = rs[4][k]
#         if v[3] == a:
#             print(v, k)
#     print()
