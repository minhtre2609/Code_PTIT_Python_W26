t = int(input())
for _ in range(t):
    s = input().strip()
    res = ""
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        res += c * int(num)
    print(res)