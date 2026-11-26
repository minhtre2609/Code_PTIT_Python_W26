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
        x = int(raw[ptr + 1])
        y = int(raw[ptr + 2])
        z = int(raw[ptr + 3])
        ptr += 4
        dp = [0] * (n + 1)
        dp[1] = x
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = min(dp[i - 1] + x, dp[i // 2] + z)
            else:
                dp[i] = min(dp[i - 1] + x, dp[(i + 1) // 2] + z + y)
        out.append(str(dp[n]))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()