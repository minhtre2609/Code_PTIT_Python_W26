n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
up = 0
down = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            up += a[i][j]
        elif i + j > n - 1:
            down += a[i][j]
diff = abs(up - down)
print("YES" if diff <= k else "NO")
print(diff)