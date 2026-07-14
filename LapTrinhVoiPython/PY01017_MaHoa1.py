t = int(input())
for _ in range(t):
    s = input().strip()
    res = ""
    i = 0
    while i < len(s):
        c = s[i]
        cnt = 1
        i += 1
        while i < len(s) and s[i] == c:
            cnt += 1
            i += 1
        res += str(cnt) + c
    print(res)