n = int(input())
s = [input().strip() for _ in range(n)]
ans = 10**9
ok = True
for target in s:
    cur = 0
    for x in s:
        if len(x) != len(target):
            ok = False
            break
        pos = (x + x).find(target)
        if pos == -1:
            ok = False
            break
        cur += pos
    if not ok:
        break
    if cur < ans:
        ans = cur
print(ans if ok else -1)