import sys
from math import gcd

toks = list(map(int, sys.stdin.read().split()))
if toks:
    t = toks[0]
    idx = 1
    out = []
    for _ in range(t):
        n = toks[idx]
        k = toks[idx + 1]
        a = toks[idx + 2 : idx + 2 + n]
        idx += 2 + n
        ans = n + 1
        for i in range(n):
            g = 0
            limit = min(n, i + ans - 1)
            for j in range(i, limit):
                g = gcd(g, a[j])
                if g < k or g % k != 0:
                    break
                if g == k:
                    ans = j - i + 1
                    break
            if ans == 1:
                break
        out.append(str(ans if ans <= n else -1))
    sys.stdout.write("\n".join(out) + "\n")