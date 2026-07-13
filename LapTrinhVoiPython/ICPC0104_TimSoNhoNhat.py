t = int(input())
for i in range(t):
    s = input()
    minn = 0
    cur = ""
    found = True
    for c in s:
        if c.isdigit():
            cur += c
        else:
            if cur != "":
                num = int(cur)
                if found or num < minn:
                    minn = num
                    found = False
                cur = ""
    if cur != "":
        num = int(cur)
        if found or num < minn:
            minn = num
    print(minn)