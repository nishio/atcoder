codes related to atcoder. MIT license.

# generate_snippets.py

generate snippets for VSCode

## `main` snippet

generate workbench for ease of development.

stored in snippets/main.py.

runtime options:

- -c: compile `solve` with numba
- `USE_NUMBA`: you need to make it True if you want to compile ahead-of-time on atcoder server
- --numba: force numba mode. use compiled library even if USE_NUMBA=False
- -p: pure python mode. not use compiled library even if USE_NUMBA=True
- -t: test mode. call `_test()` and exit without running `main`. In default, it calls doctest.
- If filename given as argument, read from it instead of sys.stdin.
- `as_input`: take string and make `read` and `input` read from the string. To use in testcase.

# testall.py

utility to test all input/output.

It assumes in/x.txt and out/x.txt are paired.
If you download testcases from atcoder's official Dropbox and unzip, it satisfied.

options:

- -f: forse all. test all testcases, even if some fails.
- -t: specify some testcases to run, comma separated.
- -p: pure python mode.
- --no-diff: suppress to print diff. see `diff_output` instead. When it is too large, it iss automatically suppressed.
