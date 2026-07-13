t = int(input())
for i in range(t):
    s = input()
    ok = True
    for j in range(len(s)):
        if (s[i] > s[i + 1]):
            ok = False
            break
    if ok: print("YES")
    else: print("NO")