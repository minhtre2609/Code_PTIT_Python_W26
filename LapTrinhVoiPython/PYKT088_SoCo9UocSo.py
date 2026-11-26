import math
from bisect import bisect_right

n = int(input())
m = math.isqrt(n)
if m < 6:
    print(0)
else:
    is_prime = bytearray([1]) * (m + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, math.isqrt(m) + 1):
        if is_prime[i]:
            is_prime[i * i :: i] = b"\x00" * ((m - i * i) // i + 1)
    primes = [i for i in range(2, m + 1) if is_prime[i]]
    ans = 0
    for p in primes:
        if p ** 8 <= n:
            ans += 1
        else:
            break
    for i, p in enumerate(primes):
        if p * p >= m:
            break
        j = bisect_right(primes, m // p)
        if j > i + 1:
            ans += j - i - 1
    print(ans)