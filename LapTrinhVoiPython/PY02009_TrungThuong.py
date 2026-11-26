t = int(input())
for _ in range(t):
    n = int(input())
    cnt = {}
    for _ in range(n):
        x = int(input())
        cnt[x] = cnt.get(x, 0) + 1
    best = min(cnt.keys(), key=lambda x: (-cnt[x], x))
    print(best)