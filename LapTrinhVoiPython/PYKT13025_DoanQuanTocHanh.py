import sys
from collections import Counter

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    cnt = Counter(int(x) for x in data[2:2 + n])
    s = sorted(cnt.values())
    m = len(s)
    best = 10**18
    max_single = s[-1]
    for p in range((m + 1) // 2, m + 1):
        rem = m - p
        if rem == 0:
            cost = p * max_single
        elif p * max_single >= best:
            continue
        else:
            paired = max(map(int.__add__, s[:rem], s[2 * rem - 1 : rem - 1 : -1]))
            cap = paired if paired > max_single else max_single
            cost = p * cap
        if cost < best:
            best = cost
    sys.stdout.write(str(best) + "\n")

if __name__ == '__main__':
    solve()