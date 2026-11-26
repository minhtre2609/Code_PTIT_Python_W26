def he_so(loai, nam):
    if loai == 'A':
        if nam <= 3: return 10
        elif nam <= 8: return 12
        elif nam <= 15: return 14
        else: return 20
    elif loai == 'B':
        if nam <= 3: return 10
        elif nam <= 8: return 11
        elif nam <= 15: return 13
        else: return 16
    elif loai == 'C':
        if nam <= 3: return 9
        elif nam <= 8: return 10
        elif nam <= 15: return 12
        else: return 14
    else:
        if nam <= 3: return 8
        elif nam <= 8: return 9
        elif nam <= 15: return 11
        else: return 13

pb = {}
n = int(input())
for _ in range(n):
    s = input().strip().split(maxsplit=1)
    pb[s[0]] = s[1]

m = int(input())
for _ in range(m):
    ma = input().strip()
    ten = input().strip()
    lcb = int(input().strip())
    nc = int(input().strip())
    
    loai = ma[0]
    nam = int(ma[1:3])
    mapb = ma[3:]
    
    hs = he_so(loai, nam)
    luong = lcb * nc * hs * 1000
    print(f"{ma} {ten} {pb[mapb]} {luong}")