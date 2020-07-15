#!/usr/bin/env python3
"""
atcoder misc commands
"""
import sys
import os
import string
from pathlib import Path
import re
import subprocess


def argv(i, default=None):
    try:
        return sys.argv[i]
    except:
        return default


if argv(1) == "gen":
    """
    create folder, files and chmod +x
    $ atcmd gen abc172
    """
    path = argv(2)
    os.makedirs(path)
    end = argv(3, "f")
    for c in string.ascii_lowercase:
        p = Path(f'{path}/{c}.py')
        p.touch()
        p.chmod(0o755)
        if c == end:
            break
    exit()

if argv(1) == "clean" or argv(1) == "comment":
    """
    comment out all debug print
    """
    path = argv(2)
    data = open(path).read()
    open(path + ".bak", "w").write(data)
    data = re.sub(r"^(\s*)debug\(", r"\1# debug(", data, 0, re.MULTILINE)
    open(path, "w").write(data)
    exit()


if argv(1) == "unclean" or argv(1) == "uncomment":
    """
    uncomment all debug print
    """
    path = argv(2)
    data = open(path).read()
    open(path + ".bak", "w").write(data)
    data = data.replace("# debug(", "debug(")
    open(path, "w").write(data)
    exit()

if argv(1) == "lprof":
    """
    call line_profiler

    kernprof -l $1.py && python3 -m line_profiler $1.py.lprof > ${2:prof}
    """
    target = argv(2)
    if not target.endswith(".py"):
        target = target + ".py"
    profname = argv(3, "prof")
    cmd = f"kernprof -l {target} && python3 -m line_profiler {target}.lprof > {profname} && code {profname}"
    subprocess.call(cmd, shell=True)
    exit()

if argv(1) == "mprof":
    """
    call memory_profiler
    """
    target = argv(2)
    if not target.endswith(".py"):
        target = target + ".py"
    profname = argv(3, "prof")
    cmd = f"mprof run {target} && mprof plot"
    print(cmd)
    subprocess.call(cmd, shell=True)
    exit()

if argv(1) == "cython":
    """
    create cython file and open
    """
    target = argv(2)
    if not target.endswith(".py"):
        target = target + ".py"
    cyfile = target.replace(".py", ".pyx")
    cmd = f"cp {target} {cyfile} && code {cyfile}"
    print(cmd)
    subprocess.call(cmd, shell=True)
    exit()

print("error: no command matched")
