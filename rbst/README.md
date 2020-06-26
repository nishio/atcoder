# e.py: segtree impl

```
test: handmade05 AC 1.277
test: handmade02 AC 0.091
test: handmade03 AC 0.089
test: handmade04 AC 0.091
test: sample01 AC 0.090
test: sample00 AC 0.086
test: handmade08 AC 4.737
test: handmade06 AC 1.674
test: handmade07 AC 1.763
test: handmade09 AC 4.708
test: random10 AC 4.235
AC: 11, max_time: 4.74
```

# main.py segtree impl

```
test: handmade05 AC 1.307
test: handmade02 AC 0.087
test: handmade03 AC 0.092
test: handmade04 AC 0.090
test: sample01 AC 0.089
test: sample00 AC 0.086
test: handmade08 AC 4.653
test: handmade06 AC 1.638
test: handmade07 AC 1.712
test: handmade09 AC 4.689
test: random10 AC 4.827
AC: 11, max_time: 4.83
```

# RBST

```
test: handmade05 AC 1.824
test: handmade02 AC 0.119
test: handmade03 AC 0.122
test: handmade04 AC 0.126
test: sample01 AC 0.112
test: sample00 AC 0.112
test: handmade08 AC 76.969
test: handmade06 AC 1.806
test: handmade07 AC 1.857
test: handmade09 AC 105.466
test: random10 AC 103.126
AC: 11, max_time: 105.47
```

# put in local

```
test: handmade05 AC 1.764
test: handmade02 AC 0.118
test: handmade03 AC 0.124
test: handmade04 AC 0.125
test: sample01 AC 0.113
test: sample00 AC 0.112
test: handmade08 AC 73.598
test: handmade06 AC 1.932
test: handmade07 AC 1.891
test: handmade09 AC 93.863
test: random10 AC 98.278
AC: 11, max_time: 98.28
```

# replace Node class into 5 lists:

```
test: handmade05 AC 1.828
test: handmade02 AC 0.125
test: handmade03 AC 0.128
test: handmade04 AC 0.142
test: sample01 AC 0.123
test: sample00 AC 0.121
test: handmade08 AC 70.420
test: handmade06 AC 1.810
test: handmade07 AC 1.870
test: handmade09 AC 83.146
test: random10 AC 100.851
AC: 11, max_time: 100.85
```

# remove useless codes

```
test: handmade05 AC 1.902
test: handmade02 AC 0.148
test: handmade03 AC 0.140
test: handmade04 AC 0.142
test: sample01 AC 0.124
test: sample00 AC 0.128
test: handmade08 AC 67.551
test: handmade06 AC 1.768
test: handmade07 AC 1.757
test: handmade09 AC 68.957
test: random10 AC 72.870
AC: 11, max_time: 72.87
```

# remove RBST class

```
test: handmade05 AC 1.652
test: handmade02 AC 0.131
test: handmade03 AC 0.133
test: handmade04 AC 0.136
test: sample01 AC 0.122
test: sample00 AC 0.121
test: handmade08 AC 65.204
test: handmade06 AC 1.848
test: handmade07 AC 1.823
test: handmade09 AC 63.355
test: random10 AC 67.006
AC: 11, max_time: 67.01
```

# remove size() / rbst_sum()

```
test: handmade05 AC 1.604
test: handmade02 AC 0.123
test: handmade03 AC 0.123
test: handmade04 AC 0.149
test: sample01 AC 0.115
test: sample00 AC 0.117
test: handmade08 AC 59.654
test: handmade06 AC 1.827
test: handmade07 AC 1.787
test: handmade09 AC 60.144
test: random10 AC 60.644
AC: 11, max_time: 60.64
```

# remove recursion of lower_bound()

```
test: handmade05 AC 1.603
test: handmade02 AC 0.117
test: handmade03 AC 0.121
test: handmade04 AC 0.127
test: sample01 AC 0.116
test: sample00 AC 0.113
test: handmade08 AC 54.097
test: handmade06 AC 1.781
test: handmade07 AC 1.844
test: handmade09 AC 54.874
test: random10 AC 57.978
AC: 11, max_time: 57.98
```

# remove recursion of upper_bound()

```
test: random10 AC 59.782
AC: 1, max_time: 59.78
```

# remove recursion of merge

```
test: handmade05 AC 1.691
test: handmade02 AC 0.122
test: handmade03 AC 0.131
test: handmade04 AC 0.132
test: sample01 AC 0.117
test: sample00 AC 0.115
test: handmade08 AC 56.759
test: handmade06 AC 1.760
test: handmade07 AC 1.790
test: handmade09 AC 57.574
test: random10 AC 64.418
AC: 11, max_time: 64.42
```

# new version of split has a bug

handmade08 > WA

https://gist.github.com/nishio/b03475b2c325c06b752f28df2f7b326c

# compare.py

handmade04

```
root: 8
values: [0, 984611856, 984611856, 984611851, 984611856, 984611858, 984611856, 984611856, 984611856, 984611856, 984611856, 984611856, 984611852, 984611856]
sizes: [0, 1, 6, 6, 3, 2, 2, 1, 13, 1, 5, 3, 2, 1]
lefts: [0, 0, 4, 0, 6, 1, 7, 0, 3, 0, 11, 12, 0, 0]
rights: [0, 0, 5, 10, 0, 0, 0, 0, 2, 0, 9, 0, 13, 0]
mismatch after insert 984611856

old_lefts: [0, 0, 4, 0, 6, 1, 7, 0, 10, 0, 11, 12, 0, 14, 0]
new_lefts: [0, 0, 4, 0, 6, 1, 7, 0, 14, 0, 11, 12, 0, 0, 3]
old_rights: [0, 0, 5, 8, 0, 0, 0, 0, 2, 0, 9, 0, 13, 0, 0]
new_rights: [0, 0, 5, 0, 0, 0, 0, 0, 2, 0, 9, 0, 13, 0, 10]
```

compress [0, 984611856, 984611856, 984611851, 984611856, 984611858, 984611856, 984611856, 984611856, 984611856, 984611856, 984611856, 984611852, 984611856] => [0, 3, 3, 1, 3, 4, 3, 3, 3, 3, 3, 3, 2, 3]

```
  "".join(f"{x:2d} " for x in xs),
```

```
                         v root
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 index
 0  3  3  1  3  4  3  3  3  3  3  3  2  3 value
 0  1  6  6  3  2  2  1 13  1  5  3  2  1 sizes
 0  0  4  0  6  1  7  0  3  0 11 12  0  0 left
 0  0  5 10  0  0  0  0  2  0  9  0 13  0 right
```

after split

```
old left [0, 0, 4, 0, 6, 1, 7, 0, 10, 0, 11, 13, 0, 0] 3 8
new left [0, 0, 4, 0, 6, 1, 7, 0, 10, 0, 11, 12, 0, 0] 3 8
```

```
split: node, k 8 2
split left
split: node, k 3 2
split right
split: node, k 10 1
split left
split: node, k 11 1
split left
split: node, k 12 1
split right
split: node, k 13 0
split left
split: node, k 0 0
old left [0, 0, 4, 0, 6, 1, 7, 0, 10, 0, 11, 13, 0, 0] 3 8
newsplit: k 2
newsplit: k 2
newsplit: k -2
newsplit: k -2
newsplit: k -2
newsplit: k -2
***new split: [True, False, True, True, True] [8, 3, 10, 11, 12]
```

bug found: https://gyazo.com/62e3a74967b4571283750eea9a724c83

# fix bug

```
test: handmade05        AC 1.705
test: handmade02        AC 0.119
test: handmade03        AC 0.125
test: handmade04        AC 0.129
test: sample01  AC 0.124
test: sample00  AC 0.116
test: handmade08        AC 60.475
test: handmade06        AC 1.936
test: handmade07        AC 1.875
test: handmade09        AC 59.571
test: random10  AC 64.489
AC: 11, max_time: 64.49
```

# compiled with numba

```
test: handmade05	AC 0.650
test: handmade02	AC 0.199
test: handmade03	AC 0.190
test: handmade04	AC 0.189
test: sample01	AC 0.195
test: sample00	AC 0.185
test: handmade08	AC 8.638
test: handmade06	AC 0.556
test: handmade07	AC 0.595
test: handmade09	AC 8.748
test: random10	AC 10.127
AC: 11, max_time: 10.13
```

# allocate in advance

```
test: handmade05	AC 0.652
test: handmade02	AC 0.198
test: handmade03	AC 0.217
test: handmade04	AC 0.206
test: sample01	AC 0.199
test: sample00	AC 0.200
test: handmade08	AC 4.394
test: handmade06	AC 0.513
test: handmade07	AC 0.549
test: handmade09	AC 4.340
test: random10	AC 4.596
AC: 11, max_time: 4.60
```

# randome_state int16

```
test: handmade05        AC 0.676
test: handmade02        AC 0.197
test: handmade03        AC 0.194
test: handmade04        AC 0.197
test: sample01  AC 0.190
test: sample00  AC 0.196
test: handmade08        AC 4.353
test: handmade06        AC 0.547
test: handmade07        AC 0.570
test: handmade09        AC 4.504
test: random10  AC 4.425
AC: 11, max_time: 4.50
```

# multi-root

```
test: handmade02        AC 0.194
test: sample01  AC 0.154
test: sample00  AC 0.175
test: handmade05_mod    AC 0.169
test: handmade03        AC 0.164
test: handmade04        AC 0.188
test: handmade05        AC 1.722
test: handmade06        AC 4.495
test: handmade07        AC 4.488
test: handmade08        AC 6.414
test: random10  AC 5.501
test: handmade09        AC 5.530
AC: 12, max_time: 6.41
```

```
time ./main.py -c
compiling

real    2m48.329s
user    2m41.474s
sys     0m4.630s
```

Pure Python mode

```
test: handmade02        AC 0.208
test: sample01  AC 0.164
test: sample00  AC 0.152
test: handmade05_mod    AC 0.154
test: handmade03        AC 0.188
test: handmade04        AC 0.217
test: handmade05        AC 42.867
test: handmade06        AC 287.386
test: handmade07        AC 263.162
test: handmade08        AC 277.958
test: random10  AC 305.557
test: handmade09        AC 308.058
AC: 12, max_time: 308.06
```
