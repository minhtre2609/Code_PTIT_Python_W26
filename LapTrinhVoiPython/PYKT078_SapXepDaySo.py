import sys

toks = list(map(int, sys.stdin.read().split()))
if toks:
    t = toks[0]
    idx = 1
    for _ in range(t):
        n = toks[idx]
        m = toks[idx + 1]
        a = toks[idx + 2 : idx + 2 + n]
        idx += 2 + n
        mx = max(a)
        pos = a.index(mx)
        a.insert(pos, m)
        neg = [x for x in a if x < 0]
        non_neg = [x for x in a if x >= 0]
        print(*(neg + non_neg))