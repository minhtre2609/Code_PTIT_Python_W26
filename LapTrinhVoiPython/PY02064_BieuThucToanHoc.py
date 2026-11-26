import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    ptr = 0
    t = int(raw[ptr])
    ptr += 1
    out = []
    base_coeffs = (1, -2, 3, -4, 5)
    for _ in range(t):
        n = int(raw[ptr])
        k = int(raw[ptr + 1])
        ptr += 2
        arr = [int(x) for x in raw[ptr:ptr + n]]
        ptr += n
        m_max = 5 * k
        if m_max == 0:
            out.append("0")
            continue
        c = [base_coeffs[i % 5] for i in range(m_max)]
        dp = [0] + [-10**18] * m_max
        for i, x in enumerate(arr):
            low = max(1, m_max - (n - 1 - i))
            high = min(m_max, i + 1)
            for m in range(high, low - 1, -1):
                v = dp[m - 1] + c[m - 1] * x
                if v > dp[m]:
                    dp[m] = v
        out.append(str(dp[m_max]))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()