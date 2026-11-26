s = input().strip()
cnt = {}
for i in range(0, len(s) - 1, 2):
    x = int(s[i:i + 2])
    cnt[x] = cnt.get(x, 0) + 1
for k, v in cnt.items():
    print(k, v)