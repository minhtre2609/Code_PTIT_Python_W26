import math

t = int(input())
a = [int(input()) for _ in range(t)]

m = max(a)

prime = [True] * (m + 1)
prime[0] = prime[1] = False

for i in range(2, math.isqrt(m) + 1):
    if prime[i]:
        for j in range(i * i, m + 1, i):
            prime[j] = False

cnt = [0] * (m + 1)

for p in range(2, m - 6):
    if prime[p]:
        if prime[p + 2] and prime[p + 6]:
            cnt[p + 6] += 1
        if prime[p + 4] and prime[p + 6]:
            cnt[p + 6] += 1

for i in range(1, m + 1):
    cnt[i] += cnt[i - 1]

for n in a:
    print(cnt[n - 1])