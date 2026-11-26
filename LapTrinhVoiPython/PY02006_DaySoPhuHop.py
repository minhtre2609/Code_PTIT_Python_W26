t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    ok = True
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
    print("YES" if ok else "NO")