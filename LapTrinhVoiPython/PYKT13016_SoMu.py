import sys
from math import isqrt

def bsgs(a, b, m):
    a %= m
    b %= m
    if m == 1:
        return 0
    if b == 1:
        return 0
    n = isqrt(m) + 1
    an = pow(a, n, m)
    vals = {}
    cur = b
    for q in range(n + 1):
        vals[cur] = q
        cur = (cur * a) % m
    cur = 1
    for p in range(1, n + 1):
        cur = (cur * an) % m
        if cur in vals:
            ans = n * p - vals[cur]
            if ans >= 0:
                return ans
    return -1

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        m = int(data[idx + 2])
        idx += 3
        out.append(str(bsgs(a, b, m)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()