n = int(input())
rows = [0] * n
cols = [0] * n
for i in range(n):
    s = input().strip()
    for j in range(n):
        if s[j] == 'C':
            rows[i] += 1
            cols[j] += 1
ans = 0
for x in rows:
    ans += x * (x - 1) // 2
for x in cols:
    ans += x * (x - 1) // 2
print(ans)