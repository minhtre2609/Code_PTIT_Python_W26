t = int(input())
for _ in range(t):
    words = input().split()
    res = ""
    for w in words:
        cand = w if not res else res + " " + w
        if len(cand.encode("utf-8")) <= 100:
            res = cand
        else:
            break
    print(res)