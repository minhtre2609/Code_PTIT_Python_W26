import sys
import bisect

MOD = 1000000007
MAX = 1000000

is_prime = bytearray([1]) * (MAX + 1)
is_prime[0] = is_prime[1] = 0
for i in range(2, 1001):
    if is_prime[i]:
        is_prime[i * i : MAX + 1 : i] = bytearray([0]) * len(range(i * i, MAX + 1, i))
primes = [i for i, val in enumerate(is_prime) if val]

def count_p(n, p):
    cnt = 0
    while n >= p:
        cnt += n // p
        n //= p
    return cnt

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    t = int(raw[0])
    ptr = 1
    out = []
    for _ in range(t):
        a = int(raw[ptr])
        b = int(raw[ptr + 1])
        ptr += 2
        ans = 1
        half = b // 2
        idx_half = bisect.bisect_right(primes, half)
        for i in range(idx_half):
            p = primes[i]
            e = count_p(b, p) - count_p(a - 1, p)
            if e > 0:
                ans = (ans * (2 * e + 1)) % MOD
        low = max(a, half + 1)
        if low <= b:
            p_cnt = bisect.bisect_right(primes, b) - bisect.bisect_left(primes, low)
            if p_cnt > 0:
                ans = (ans * pow(3, p_cnt, MOD)) % MOD
        out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()