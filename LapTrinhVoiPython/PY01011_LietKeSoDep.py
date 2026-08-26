t = int(input())
for i in range(t):
    n = int(input())
    for i in range (22, n, 2):
        s = str(i)
        if len(s) % 2 == 1: continue
        if s != s[::-1]: continue
        ok = True
        for j in s:
            if j not in "02468":
                ok = False
                break
        if ok: print(i, end = " ")
    print()