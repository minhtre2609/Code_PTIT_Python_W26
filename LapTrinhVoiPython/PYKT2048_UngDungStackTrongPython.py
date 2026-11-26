import sys

def count_at_most(s, max_d):
    if max_d < 0:
        return 0
    dp = [0] * (max_d + 1)
    dp[0] = 1
    for ch in s:
        ndp = [0] * (max_d + 1)
        if ch == '(':
            for d in range(max_d):
                ndp[d + 1] = dp[d]
        elif ch == ')':
            for d in range(1, max_d + 1):
                ndp[d - 1] = dp[d]
        else:
            for d in range(max_d + 1):
                v = dp[d]
                if v:
                    if d + 1 <= max_d:
                        ndp[d + 1] += v
                    if d > 0:
                        ndp[d - 1] += v
        dp = ndp
    return dp[0]

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    k = int(data[0])
    s = data[1]
    if len(s) & 1:
        sys.stdout.write("0\n")
        return
    ans = count_at_most(s, k) - count_at_most(s, k - 1)
    sys.stdout.write(str(ans) + "\n")

if __name__ == '__main__':
    solve()