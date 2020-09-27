"""
Suffix Array: SA-IS + Kasai LCP

SA-IS for Suffix Array Construction
(derived from https://mametter.hatenablog.com/entry/20180130/p1)
Kasai Method for LCP array Construction
(derived from http://www.nct9.ne.jp/m_hiroi/light/pyalgo60.html)
"""

SMALLER = 0
LARGER = 1


def get_ls(seq):
    "smaller: 0, larger: 1"
    N = len(seq)
    ls = [SMALLER] * N
    # sentinel is the smallest
    # ls[-1] = SMALLER

    for i in range(N - 2, -1, -1):
        # s[i] < s[i+1] なら明らかに s[i..] < s[i+1..] => i は S 型
        # s[i] > s[i+1] なら明らかに s[i..] > s[i+1..] => i は L 型
        # s[i] == s[i+1] の場合、s[i..] <=> s[i+1..] の比較結果は
        # s[i+1..] <=> s[i+2..] に準ずる (つまり ls[i + 1] と同じ)
        if seq[i] < seq[i + 1]:
            ls[i] = SMALLER
        elif seq[i] > seq[i + 1]:
            ls[i] = LARGER
        else:
            ls[i] = ls[i + 1]
    return ls


def get_lmss(ls):
    """
    >>> get_lmss(get_ls("mmiissiissiippii$"))
    [2, 6, 10, 16]
    """
    return [i for i in range(len(ls)) if is_lms(ls, i)]


def is_lms(ls, i):
    # インデックス i が LMS かどうか
    return (i > 0 and ls[i - 1] == LARGER and ls[i] == SMALLER)


def sa_is(seq, K=256):
    """
    >>> sa_is(b"mmiissiissiippii$", 256)
    [16, 15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4]
    >>> sa_is([2, 2, 1, 0], 3)
    [3, 2, 1, 0]
    """
    # L 型か S 型かのテーブル
    ls = get_ls(seq)
    # LMS のインデックスだけを集めた配列
    lmss = get_lmss(ls)
    # 適当な「種」：seed = lmss.shuffle でもよい
    seed = lmss

    # 1 回目の induced sort
    sa = induced_sort(seq, K, ls, seed)

    # induced sort の結果から LMS の suffix だけ取り出す
    sa = [i for i in sa if is_lms(ls, i)]

    # LMS のインデックス i に対して番号 nums[i] を振る
    nums = [None] * len(seq)

    # sa[0] の LMS は $ と決まっているので、番号 0 を振っておく
    nums[sa[0]] = num = 0

    # 隣り合う LMS を比べる
    for index in range(1, len(sa)):
        i = sa[index - 1]
        j = sa[index]
        isDifferent = False
        # 隣り合う LMS 部分文字列の比較
        for d in range(len(seq)):
            if seq[i + d] != seq[j + d] or is_lms(ls, i + d) != is_lms(ls, j + d):
                # LMS 部分文字列の範囲で異なる文字があった
                isDifferent = True
                break
            if d > 0 and (is_lms(ls, i + d) or is_lms(ls, j + d)):
                # LMS 部分文字列の終端に至った
                break
        # 隣り合う LMS 部分文字列が異なる場合は、番号を増やす
        if isDifferent:
            num += 1
        # LMS のインデックス j に番号 num を振る
        nums[j] = num

    # nums の中に出現する番号のみを並べると、LMS 部分文字列を番号に置き換えた列が得られる
    # remove None from nums
    nums = list(filter(lambda x: x is not None, nums))

    if num + 1 < len(nums):
        # 番号の重複があるので再帰
        sa = sa_is(nums, num + 1)
    else:
        # 番号の重複がない場合、suffix array を容易に求められる
        sa = [None] * len(nums)
        for i, c in enumerate(nums):
            sa[c] = i

    # 正しい「種」
    seed = [lmss[i] for i in sa]

    # 2 回目の induced sort
    sa = induced_sort(seq, K, ls, seed)
    return sa


def induced_sort(seq, K, ls, lmss, verbose=False):
    """
    >>> seq = b"mmiissiissiippii$"
    >>> ls = get_ls(seq)
    >>> lmss = get_lmss(ls)
    >>> induced_sort(seq, 256, ls, lmss, verbose=True)
    step1: [16, None, None, None, None, None, 2, 6, 10, None, None, None, None, None, None, None, None]
    step2: [16, 15, 14, None, None, None, 2, 6, 10, 1, 0, 13, 12, 5, 9, 4, 8]
    step3: [16, 15, 14, 10, 2, 6, 11, 3, 7, 1, 0, 13, 12, 5, 9, 4, 8]
    """
    # 作業領域
    sa = [None] * len(seq)

    # seq に出現する文字種ごとのカウント
    count = [0] * K
    for c in seq:
        count[c] += 1

    # 累積和することで bin の境界インデックスを決める
    # 文字種cのbinはbin[c - 1] <= i < bin[c]
    # c is 0-origin
    from itertools import accumulate
    bin = list(accumulate(count)) + [0]

    # ステップ 1: LMS のインデックスをビンの終わりの方から入れる

    # ビンごとにすでに挿入した数をカウントする
    count_in_bin = [0] * K

    for lms in reversed(lmss):
        c = seq[lms]
        # c を入れるビンの終わり (bin[c] - 1) から詰めていれる
        pos = bin[c] - 1 - count_in_bin[c]
        sa[pos] = lms
        count_in_bin[c] += 1

    if verbose:
        print("step1:", sa)

    # ステップ 2: sa を昇順に走査していく

    # ビンごとにすでに挿入した数をカウントする
    count_in_bin = [0] * K

    for i in sa:
        if i is None:
            continue
        if i == 0:
            continue
        if ls[i - 1] == SMALLER:
            continue
        # sa に入っているインデックス i について、i - 1 が L 型であるとき、
        # 文字 seq[i - 1] に対応するビンに i - 1 を頭から詰めていれる
        c = seq[i - 1]
        pos = bin[c - 1] + count_in_bin[c]
        sa[pos] = i - 1
        count_in_bin[c] += 1

    if verbose:
        print("step2:", sa)

    # ステップ 3: sa を逆順に走査していく

    # ビンごとにすでに挿入した数をカウントする
    count_in_bin = [0] * K

    for i in reversed(sa):
        if i is None:
            continue
        if i == 0:
            continue
        if ls[i - 1] == LARGER:
            continue

        # sa に入っているインデックス i について、i - 1 が S 型であるとき、
        # 文字 seq[i - 1] に対応するビンに i - 1 を終わりから詰めていれる
        c = seq[i - 1]
        pos = bin[c] - 1 - count_in_bin[c]
        sa[pos] = i - 1  # 上書きすることもある
        count_in_bin[c] += 1

    if verbose:
        print("step3:", end=" ")

    return sa


def get_height(seq, sa):
    """
    Kasai method
    >>> s = b"banana$"
    >>> sa = sa_is(s, 256)
    >>> get_height(s, sa)
    [0, 1, 3, 0, 0, 2, -1]
    """
    N = len(sa)
    rsa = [0] * N
    for i in range(N):
        rsa[sa[i]] = i

    def lcp(i, j):
        d = 0
        while seq[i + d] == seq[j + d]:
            d += 1
        return d

    height = [0] * N
    h = 0
    for i in range(N):
        j = rsa[i]
        if j == N - 1:  # last
            height[j] = -1
            h = 0
            continue
        k = sa[j + 1]
        if h > 0:
            h = h - 1 + lcp(i + h - 1, k + h - 1)
        else:
            h = lcp(i, k)
        height[j] = h

    return height


def suffix_array(seq, K):
    return sa_is(seq, K)


def lcp_array(seq, sa):
    return get_height(seq, sa)

# --- end of library ---


def debug(*x):
    print(*x, file=sys.stderr)


def solve(S):
    diff = ord("a") - 1
    N = len(S)
    S = [c - diff for c in S]
    S.append(0)
    lcp = lcp_array(S, suffix_array(S, 27))
    return N * (N + 1) // 2 - sum(lcp) - 1


def main():
    # parse input
    S = input().strip()
    print(solve(S))


# tests
T1 = """
abcbcba
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
21
"""

T2 = """
mississippi
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
53
"""

T3 = """
ababacaca
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
33
"""

T4 = """
aaaaa
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
5
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
