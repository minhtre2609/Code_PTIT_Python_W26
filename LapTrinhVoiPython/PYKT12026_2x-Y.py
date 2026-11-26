import sys
from math import gcd

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        a0 = int(data[idx + 2])
        g = 0
        for j in range(1, n):
            g = gcd(g, abs(int(data[idx + 2 + j]) - a0))
        idx += 2 + n
        if g == 0:
            out.append("YES" if k == a0 else "NO")
        else:
            out.append("YES" if (k - a0) % g == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()