t = int(input())
for k in range(t):
    s = input()
    ok = True
    for i in range(len(s)):
        if (s[i] != '0' and s[i] != '1' and s[i] != '2'):
            ok = False
            break
    if (ok == True): print("YES")
    else: print("NO")