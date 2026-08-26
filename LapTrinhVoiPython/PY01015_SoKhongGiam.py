t = int(input())

for i in range(t):
    s = input()
    ok = True
    for j in range(len(s) - 1):
        if s[j] > s[j + 1]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")