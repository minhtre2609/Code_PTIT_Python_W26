def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
p = sorted([x for x in a if is_prime(x)])
idx = 0
for i in range(n):
    if is_prime(a[i]):
        a[i] = p[idx]
        idx += 1
print(*a)