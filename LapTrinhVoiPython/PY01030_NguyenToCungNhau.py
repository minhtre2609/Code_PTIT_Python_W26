import math

n, k = map(int, input().split())
start = 10**(k - 1)
end = 10**(k)
cnt = 0
res = []
for i in range(start, end):
    if math.gcd(i, n) == 1:
        res.append(str(i))
        cnt += 1
        if (cnt == 10):
            print(' '.join(res))
            res = []
            cnt = 0
if res:
    print(' '.join(res))