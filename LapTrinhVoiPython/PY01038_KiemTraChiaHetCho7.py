t = int(input())
for i in range(t):
    n = int(input())
    if n % 7 == 0:
        print(n)
        continue
    ok = False
    for _ in range(1000):
        n += int(str(n)[::-1])
        if (n % 7 == 0):
            print(n)
            ok = True
            break
    if not ok:
        print(-1)