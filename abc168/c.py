import sys
from math import sin, cos, pi, sqrt
S = sys.stdin.read()
A, B, H, M = [int(x) for x in S.split()]

angle_a = 2 * pi / 60 * M
angle_b = 2 * pi * (H / 12 + M / 60 / 12)
ax = sin(angle_a) * A
ay = cos(angle_a) * A
bx = sin(angle_b) * B
by = cos(angle_b) * B
d = sqrt((ax - bx) ** 2 + (ay - by) ** 2)
print(d)
