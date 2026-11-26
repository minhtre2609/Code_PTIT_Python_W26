def chuan_hoa(name):
    words = name.strip().split()
    return ' '.join(w.capitalize() for w in words)

n = int(input())
ds = []
for i in range(1, n + 1):
    ma = f"TS{i:02d}"
    ten = chuan_hoa(input())
    diem = float(input())
    dt = input().strip()
    kv = int(input().strip())
    
    ut = 0
    if kv == 1:
        ut += 1.5
    elif kv == 2:
        ut += 1.0
    
    if dt != "Kinh":
        ut += 1.5
    
    tong = diem + ut
    tt = "Do" if tong >= 20.5 else "Truot"
    ds.append((ma, ten, tong, tt))

ds.sort(key=lambda x: (-x[2], x[0]))

for x in ds:
    print(f"{x[0]} {x[1]} {x[2]:.1f} {x[3]}")