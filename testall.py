#!/usr/bin/env python3
"""
utility to test all input/output

It assumes in/x.txt and out/x.txt are paired.
If you download testcases from atcoder's official Dropbox and unzip, it satisfied.
"""
import sys
import subprocess
import os
import time
import argparse

parser = argparse.ArgumentParser(description='Test all')
parser.add_argument('target_script', type=str)
parser.add_argument(
    "-f", "--force-all", action="store_true",
    help="even if some test fail, run all")
parser.add_argument(
    "-t", "--test", action="store",
    help="specify testcase filename")

parser.add_argument(
    "-p", "--pure-python", action="store_true",
    help="pass target an option `-p`")

args = parser.parse_args()

target = args.target_script
max_time = 0
num_ac = 0
num_wa = 0
num_re = 0
if args.test:
    test = [x.replace("in/", "") for x in args.test.split(",")]
else:
    test = os.listdir("in")

PURE_PYTHON = "-p" if args.pure_python else ""


for f in test:
    print(f"test: {f}", end="\t")
    t = time.perf_counter()
    ret = subprocess.call(
        f"python3 {target} {PURE_PYTHON} <in/{f} > output", shell=True)
    t = time.perf_counter() - t
    if ret:
        print("RE")
        num_re += 1
        if not args.force_all:
            break
        continue
    ret = subprocess.call(f"diff output out/{f}", shell=True)
    if ret:
        print("WA")
        num_wa += 1
        if not args.force_all:
            break
        continue
    print(f"AC {t:.3f}")
    num_ac += 1
    max_time = max(max_time, t)

msg = f"AC: {num_ac}"
if num_wa:
    msg += f", WA: {num_wa}"
if num_re:
    msg += f", RE: {num_re}"
msg += f", max_time: {max_time:.2f}"
print(msg)
