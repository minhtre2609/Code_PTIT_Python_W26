def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
res = 0
for x in a:
    d = 0
    while not is_prime(x - d) and not is_prime(x + d):
        d += 1
    if d > res:
        res = d
print(res)