n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
up = 0
down = 0
for i in range(n):
    for j in range(n):
        if j > i:
            up += a[i][j]
        elif j < i:
            down += a[i][j]
diff = abs(up - down)
print("YES" if diff <= k else "NO")
print(diff)