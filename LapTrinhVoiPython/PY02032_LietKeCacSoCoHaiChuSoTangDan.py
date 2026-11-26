s = input().strip()
res = set()
for i in range(0, len(s) - 1, 2):
    res.add(int(s[i:i + 2]))
print(*sorted(res))