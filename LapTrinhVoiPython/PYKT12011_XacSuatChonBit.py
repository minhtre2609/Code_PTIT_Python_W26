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
        s = data[idx + 2]
        idx += 3
        pref = [0] * (n + 1)
        c = 0
        for i, ch in enumerate(s):
            if ch == '1':
                c += 1
            pref[i + 1] = c
        cnt = 0
        for i, ch in enumerate(s):
            if ch == '1':
                l = 0 if i - k < 0 else i - k
                r = n - 1 if i + k >= n else i + k
                cnt += pref[r + 1] - pref[l]
        if cnt == 0:
            out.append("0/1")
        else:
            tot = n * n
            g = gcd(cnt, tot)
            out.append(f"{cnt // g}/{tot // g}")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()