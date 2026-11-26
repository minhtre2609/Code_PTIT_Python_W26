import sys
import math

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    n = int(d[0])
    m = int(d[1])
    a = [int(x) for x in d[2:n+2]]
    s = m - sum(a)
    if s < 0:
        print(0)
    else:
        mod = 10**9 + 7
        ans = math.comb(s + n - 1, n - 1) % mod
        print(ans)

if __name__ == '__main__':
    solve()