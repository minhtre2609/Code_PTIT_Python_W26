import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1][:n]
    mod = 1000000007
    bit_len = [v.bit_length() for v in range(21)]
    total_cost = [0] * 21
    for v in range(1, 21):
        total_cost[v] = total_cost[v - 1] + bit_len[v]

    dp = [{} for _ in range(n + 1)]
    ans = 0
    valid_masks = [(1 << m) - 1 for m in range(1, 21)]
    cost_cache = {0: 0}
    req_cache = {0: 0}
    for i in range(n):
        cur = dp[i]
        for m in valid_masks:
            if m in cur:
                ans = (ans + cur[m]) % mod
        cur[0] = (cur.get(0, 0) + 1) % mod
        val = 0
        for j in range(i + 1, n + 1):
            val = (val << 1) | (1 if s[j - 1] == '1' else 0)
            if val > 20:
                break
            if val >= 1:
                bit = 1 << (val - 1)
                bl = bit_len[val]
                rem = n - j
                nxt = dp[j]
                for mask, cnt in cur.items():
                    nmask = mask | bit
                    req = req_cache.get(nmask)
                    if req is None:
                        c = cost_cache[mask] + bl
                        cost_cache[nmask] = c
                        req = total_cost[nmask.bit_length()] - c
                        req_cache[nmask] = req
                    if req <= rem:
                        nxt[nmask] = (nxt.get(nmask, 0) + cnt) % mod
        dp[i] = None
    for m in valid_masks:
        if m in dp[n]:
            ans = (ans + dp[n][m]) % mod
    sys.stdout.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()