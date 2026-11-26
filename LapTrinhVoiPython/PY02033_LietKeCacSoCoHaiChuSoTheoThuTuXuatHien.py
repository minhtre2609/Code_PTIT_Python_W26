s = input().strip()
res = []
seen = set()
for i in range(0, len(s) - 1, 2):
    x = int(s[i:i + 2])
    if x not in seen:
        seen.add(x)
        res.append(x)
print(*res)