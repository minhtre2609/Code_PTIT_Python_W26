def chuan_hoa(name):
    return ' '.join(w.capitalize() for w in name.strip().split())

def get_dm(loai):
    if loai == 'A': return 100
    elif loai == 'B': return 500
    else: return 200

n = int(input())
ds = []
for i in range(1, n + 1):
    ma = f"KH{i:02d}"
    ten = chuan_hoa(input())
    parts = input().strip().split()
    loai = parts[0]
    dau = int(parts[1])
    cuoi = int(parts[2])
    
    so_dien = cuoi - dau
    dm = get_dm(loai)
    
    if so_dien < dm:
        trong_dm = so_dien * 450
        vuot_dm = 0
    else:
        trong_dm = dm * 450
        vuot_dm = (so_dien - dm) * 1000
    
    vat = vuot_dm // 20
    tong = trong_dm + vuot_dm + vat
    ds.append((ma, ten, trong_dm, vuot_dm, vat, tong))

ds.sort(key=lambda x: -x[5])

for x in ds:
    print(f"{x[0]} {x[1]} {x[2]} {x[3]} {x[4]} {x[5]}")