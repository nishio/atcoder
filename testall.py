#!/usr/bin/env python3

import sys
import subprocess
import os
import time

print(sys.argv)
if len(sys.argv) == 1:
    target = "main.py"
else:
    target = sys.argv[1]

for f in os.listdir("in"):
    print(f"test: {f}", end="\t")
    t = time.perf_counter()
    ret = subprocess.call(
        f"python3 {target} <in/{f} > output", shell=True)
    t = time.perf_counter() - t
    if ret:
        print("RE")
        break
    ret = subprocess.call(f"diff output out/{f}", shell=True)
    if ret:
        print("WA")
        break
    print(f"AC {t:.3f}")
