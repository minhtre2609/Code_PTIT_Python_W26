import sys

MOD = 1000000007
toks = list(map(int, sys.stdin.read().split()))
if toks:
    t = toks[0]
    out = []
    idx = 1
    for _ in range(t):
        n = toks[idx]
        k = toks[idx + 1]
        idx += 2
        res = 0
        for ch in bin(k)[2:]:
            res = (res * n + (ch == "1")) % MOD
        out.append(str(res))
    sys.stdout.write("\n".join(out) + "\n")