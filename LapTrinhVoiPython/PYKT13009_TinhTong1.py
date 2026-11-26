MOD = 10**9 + 7

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        y = [0] * (k + 3)
        cur = 0
        for i in range(1, k + 3):
            cur = (cur + pow(i, k, MOD)) % MOD
            y[i] = cur
            
        if n <= k + 2:
            print(y[n])
            continue
            
        m = k + 2
        fact = [1] * (m + 1)
        inv = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        inv[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m - 1, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % MOD
            
        pref = [1] * (m + 2)
        suff = [1] * (m + 2)
        for i in range(1, m + 1):
            pref[i] = (pref[i - 1] * (n - i)) % MOD
        for i in range(m, 0, -1):
            suff[i] = (suff[i + 1] * (n - i)) % MOD
            
        ans = 0
        for i in range(1, m + 1):
            num = (pref[i - 1] * suff[i + 1]) % MOD
            den = (inv[i - 1] * inv[m - i]) % MOD
            term = (y[i] * num) % MOD
            term = (term * den) % MOD
            if (m - i) % 2 == 1:
                ans = (ans - term + MOD) % MOD
            else:
                ans = (ans + term) % MOD
                
        print(ans)

solve()