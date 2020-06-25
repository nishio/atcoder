# generate_snippets.py

## main

- -c: compile `solve` with numba
- USE_NUMBA: you need to be True if you want to compile on atcoder server
- -p: pure python mode. not use compiled library even if USE_NUMBA=True
- --numba: force numba mode. use compiled library even if USE_NUMBA=False
- -t: test mode. call `_test()` and exit without run `main`
- given filename as argument, read from it instead of sys.stdin.

# testall.py

- -f: forse all. test all testcases, even if some fails.
- -t: specify some testcases to run, comma separated.
- -p: pure python mode.
- --no-diff: suppress output of diff
