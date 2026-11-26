def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = []
seen = set()
for x in a:
    if x not in seen:
        seen.add(x)
        b.append(x)
total = sum(b)
left = 0
ans = -1
for i in range(len(b)):
    left += b[i]
    if is_prime(left) and is_prime(total - left):
        ans = i
        break
print(ans if ans != -1 else "NOT FOUND")