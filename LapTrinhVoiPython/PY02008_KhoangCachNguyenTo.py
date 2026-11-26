def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

n, x = map(int, input().split())
res = [x]
cur = 2
while len(res) <= n:
    if is_prime(cur):
        res.append(res[-1] + cur)
    cur += 1
print(*res)