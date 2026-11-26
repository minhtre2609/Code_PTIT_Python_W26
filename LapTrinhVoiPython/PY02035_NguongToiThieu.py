s = input().strip()
k = int(input())
cnt = {}
for i in range(0, len(s) - 1, 2):
    x = int(s[i:i + 2])
    cnt[x] = cnt.get(x, 0) + 1
res = sorted((x, v) for x, v in cnt.items() if v >= k)
if not res:
    print("NOT FOUND")
else:
    for x, v in res:
        print(x, v)