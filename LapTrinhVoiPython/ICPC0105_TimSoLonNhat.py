t = int(input())
for i in range(t):
    s = input()
    maxx = 100005
    cur = ""
    found = True
    for c in s:
        if c.isdigit():
            cur += c
        else:
            if cur != "":
                num = int(cur)
                if found or num > maxx:
                    maxx = num
                    found = False
                cur = ""
    if cur != "":
        num = int(cur)
        if found or num > maxx:
            maxx = num
    print(maxx)