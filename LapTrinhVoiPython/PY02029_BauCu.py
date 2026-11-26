n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = {}
for x in a:
    cnt[x] = cnt.get(x, 0) + 1
vals = sorted(set(cnt.values()), reverse=True)
if len(vals) < 2:
    print("NONE")
else:
    sec = vals[1]
    res = min(k for k, v in cnt.items() if v == sec)
    print(res)