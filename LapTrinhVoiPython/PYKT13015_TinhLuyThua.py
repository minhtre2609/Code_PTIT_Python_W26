import sys

LIMIT = 3163
isp = bytearray([1]) * (LIMIT + 1)
isp[0] = isp[1] = 0
for i in range(2, int(LIMIT**0.5) + 1):
    if isp[i]:
        isp[i * i : LIMIT + 1 : i] = bytearray(len(isp[i * i : LIMIT + 1 : i]))
primes = [i for i, v in enumerate(isp) if v]
phi_cache = {}

def get_phi(m):
    if m in phi_cache:
        return phi_cache[m]
    orig = m
    res = m
    for p in primes:
        if p * p > m:
            break
        if m % p == 0:
            res -= res // p
            while m % p == 0:
                m //= p
    if m > 1:
        res -= res // m
    phi_cache[orig] = res
    return res

def pow_cap(c, d, cap):
    if d == 0:
        return 1
    if c == 0:
        return 0
    if c == 1:
        return 1
    res = 1
    for _ in range(d):
        res *= c
        if res >= cap:
            return cap
    return res

def solve_one(a, b, c, d, m):
    if m == 1:
        return 0
    if b == 0:
        return 1 % m
    if c == 0 and d > 0:
        return 1 % m
    a %= m
    if a == 0:
        return 0
    if a == 1:
        return 1
    phi = get_phi(m)
    cap = pow_cap(c, d, 25)
    if b * cap < 25:
        return pow(a, b * (c ** d), m)
    e = (b % phi) * pow(c, d, phi) % phi + phi
    return pow(a, e, m)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        d = int(data[idx + 3])
        m = int(data[idx + 4])
        idx += 5
        out.append(str(solve_one(a, b, c, d, m)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()