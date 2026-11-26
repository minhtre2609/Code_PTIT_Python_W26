def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

n, m = map(int, input().split())
for _ in range(n):
    row = list(map(int, input().split()))
    print(*[1 if is_prime(x) else 0 for x in row])