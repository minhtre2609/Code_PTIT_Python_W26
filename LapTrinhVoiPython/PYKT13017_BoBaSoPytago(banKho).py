import sys

def f0_fast(p, k):
    ans = 0
    for j in range(k // 2 + 1):
        rem = k - 2 * j
        if rem == 0:
            u = 1
        elif p == 2:
            if rem == 1:
                u = 4
            elif rem == 2:
                u = 16
            else:
                u = 1 << (2 * rem)
        else:
            if rem == 1:
                u = p * p
            else:
                u = (p ** (2 * rem - 2)) * (p * p - 1)
        ans += (p ** (3 * j)) * u
    return ans

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    temp = n
    f = 1
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            k = 0
            while temp % p == 0:
                temp //= p
                k += 1
            f *= f0_fast(p, k)
        p += 1
    if temp > 1:
        f *= f0_fast(temp, 1)
    cnt1 = [0] * n
    for x in range(1, n):
        cnt1[(x * x) % n] += 1
    z1 = cnt1[0]
    for r in range(n):
        c = cnt1[r]
        if c:
            f -= 2 * c * c + c * cnt1[(n - r) % n]
    f -= 1 + 3 * z1
    diag = sum(cnt1[(2 * a * a) % n] for a in range(1, n))
    sys.stdout.write(str((f + diag) // 2) + "\n")

if __name__ == '__main__':
    solve()