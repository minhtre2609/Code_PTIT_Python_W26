s = input().strip()
if (s[0] == '-'): s = s[1:]
cnt = 0
while len(s) > 1:
    tong = 0
    for i in s:
        tong += int(i)
    s = str(tong)
    cnt += 1
print(cnt)