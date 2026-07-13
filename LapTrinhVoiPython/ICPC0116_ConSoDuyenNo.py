t = int(input())
for i in range(t):
    s = input()
    ok = False
    for i in range (len(s)):
        if (s[0] == s[len(s) - 1]):
            ok = True
    if (ok == True):
        print('YES')
    else:
        print('NO')