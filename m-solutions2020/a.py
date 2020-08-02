#!/usr/bin/env python3

X = int(input())
for i, v in enumerate([1800, 1600, 1400, 1200, 1000, 800, 600, 400]):
    if X >= v:
        print(i + 1)
        break
