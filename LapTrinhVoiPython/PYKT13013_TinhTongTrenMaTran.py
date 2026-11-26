import sys

MOD = 1000000007
INV2 = 500000004

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    idx = 3
    rows = {}
    cols = {}
    for _ in range(k):
        t = data[idx]
        x = int(data[idx + 1])
        y = int(data[idx + 2]) % MOD
        idx += 3
        if t == 'R':
            rows[x] = rows.get(x, 1) * y % MOD
        else:
            cols[x] = cols.get(x, 1) * y % MOD
    sum_r = n % MOD
    sum_ir = (n - 1) * n // 2 % MOD
    for x, r in rows.items():
        d = (r - 1) % MOD
        sum_r = (sum_r + d) % MOD
        sum_ir = (sum_ir + (x - 1) * d) % MOD
    sum_c = m % MOD
    sum_jc = m * (m + 1) // 2 % MOD
    for y, c in cols.items():
        d = (c - 1) % MOD
        sum_c = (sum_c + d) % MOD
        sum_jc = (sum_jc + y * d) % MOD
    ans = (m % MOD * sum_ir % MOD * sum_c + sum_r * sum_jc) % MOD
    sys.stdout.write(str(ans) + "\n")

if __name__ == '__main__':
    solve()