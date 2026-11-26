import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    inf = 10 ** 9
    for _ in range(t):
        n = int(data[idx])
        arr = [int(x) for x in data[idx + 1:idx + 1 + n]]
        idx += 1 + n
        arr.sort()
        dp = [inf] * (n + 1)
        dp[0] = 0
        for tm in range(1, 2 * n + 1):
            limit = n if tm > n else tm
            for i in range(limit, 0, -1):
                c = dp[i - 1] + abs(arr[i - 1] - tm)
                if c < dp[i]:
                    dp[i] = c
        out.append(str(dp[n]))
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()