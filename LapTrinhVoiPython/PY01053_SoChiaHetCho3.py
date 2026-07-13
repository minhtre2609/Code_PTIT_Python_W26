t = int(input())
for i in range(t):
    s = input()
    tong = 0
    for c in s:
        tong += int(c)
    if (tong % 3 == 0): print('YES')
    else: print('NO')
