import sys

MOD = 10**9 + 7

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    a = [int(x) for x in data[2:n+2]]
    a.sort()
    
    fact = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD
        
    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return (fact[n] * inv[r] % MOD) * inv[n - r] % MOD

    ans = 0
    for i in range(n):
        c_max = comb(i, k - 1)
        c_min = comb(n - 1 - i, k - 1)
        term = ((c_max - c_min + MOD) % MOD * a[i]) % MOD
        ans = (ans + term) % MOD
        
    print(ans)

solve()