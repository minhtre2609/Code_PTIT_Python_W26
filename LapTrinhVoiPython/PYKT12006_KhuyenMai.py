n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

items = []
for i in range(n):
    items.append((a[i] - b[i], a[i], b[i]))

items.sort(key=lambda x: x[0])

ans = 0
for i in range(k):
    ans += items[i][1]

for i in range(k, n):
    if items[i][0] < 0:
        ans += items[i][1]
    else:
        ans += items[i][2]

print(ans)