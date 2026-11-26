import math

def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = exgcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def crt(r1, m1, r2, m2):
    g, p, q = exgcd(m1, m2)
    if (r2 - r1) % g != 0:
        return None, None
    m = (m1 * m2) // g
    k = (r2 - r1) // g
    x = (r1 + k * p % (m2 // g) * m1) % m
    return (x % m + m) % m, m

t = int(input())
for _ in range(t):
    a, b, x, y, z, l, r = map(int, input().split())
    vols = set()
    for h in range(1, (min(a, b) + 1) // 2):
        v = (a - 2 * h) * (b - 2 * h) * h
        if v > 0:
            vols.add(v)
            
    top3 = sorted(list(vols), reverse=True)[:3]
    v1, v2, v3 = top3[0], top3[1], top3[2]
    
    rem1, mod1 = crt(x, v1, y, v2)
    if rem1 is None:
        print(-1)
        continue
    rem, mod = crt(rem1, mod1, z, v3)
    if rem is None:
        print(-1)
        continue
        
    ans = -1
    if rem >= l:
        k = 0
        cur = rem
    else:
        k = math.ceil((l - rem) / mod)
        cur = rem + k * mod
        
    if cur <= r:
        ans = cur
        
    print(ans)