import sys

c8 = [0] * 1000
s8 = [0] * 1000
pc = [0] * 1001
ps = [0] * 1001
for r in range(0, 1000, 8):
    c8[r] = 1
    d2 = r // 100
    d1 = (r // 10) % 10
    d0 = r % 10
    s8[r] = (1 if d2 in (6, 8) else 0) + (1 if d1 in (6, 8) else 0) + (1 if d0 in (6, 8) else 0)
for i in range(1000):
    pc[i + 1] = pc[i] + c8[i]
    ps[i + 1] = ps[i] + s8[i]

P10 = [10 ** i for i in range(20)]

def count_68_upto(m):
    if m <= 0:
        return 0
    s = str(m)
    L = len(s)
    ans = 0
    ones = 0
    for i, ch in enumerate(s):
        d = ord(ch) - 48
        rem = L - 1 - i
        p10 = P10[rem]
        if d > 0:
            ans += d * ones * p10
            if rem > 0:
                ans += d * 2 * rem * P10[rem - 1]
            if d > 6:
                ans += p10
            if d > 8:
                ans += p10
        if d == 6 or d == 8:
            ones += 1
    ans += ones
    return ans

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for idx in range(1, t + 1):
        N = int(data[idx])
        if N < 8:
            out.append("0")
        elif N < 1000:
            out.append(str(ps[N + 1]))
        else:
            q = N // 1000
            r = N % 1000
            ans = q * 106 + ps[r + 1]
            if q > 1:
                ans += 125 * count_68_upto(q - 1)
            sq = str(q)
            q_68 = sq.count('6') + sq.count('8')
            ans += q_68 * pc[r + 1]
            out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()