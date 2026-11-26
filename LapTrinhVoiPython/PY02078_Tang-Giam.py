import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    ptr = 0
    t = int(raw[ptr])
    ptr += 1
    out = []
    for _ in range(t):
        n = int(raw[ptr])
        ptr += 1
        a = []
        b = []
        for _ in range(n):
            a.append(float(raw[ptr]))
            b.append(float(raw[ptr + 1]))
            ptr += 2
        dp = [1] * n
        ans = 1
        for i in range(n):
            ai = a[i]
            bi = b[i]
            dpi = 1
            for j in range(i):
                if a[j] < ai and b[j] > bi:
                    if dp[j] + 1 > dpi:
                        dpi = dp[j] + 1
            dp[i] = dpi
            if dpi > ans:
                ans = dpi
        out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()