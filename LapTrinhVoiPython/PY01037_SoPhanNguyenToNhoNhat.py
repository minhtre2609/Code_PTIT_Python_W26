from bisect import bisect_left
import sys

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
limit = 20000000
a = []

def dfs(i, last, cur, d):
    a.append((cur, d))
    if i == len(primes):
        return
    x = cur
    for e in range(1, last + 1):
        x *= primes[i]
        if x > limit:
            break
        dfs(i + 1, e, x, d * (e + 1))

dfs(0, 60, 1, 1)

a.sort()

b = []
mx = 0
for n, d in a:
    if d > mx:
        mx = d
        b.append(n)

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x = int(input())
    print(b[bisect_left(b, x)])