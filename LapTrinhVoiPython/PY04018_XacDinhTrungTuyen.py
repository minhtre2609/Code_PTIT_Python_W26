mon_hoc = {'A': 'TOAN', 'B': 'LY', 'C': 'HOA'}
uu_tien = {'1': 2.0, '2': 1.5, '3': 1.0, '4': 0.0}

class GiaoVien:
    def __init__(self, ma, ten, maxt, tin, cm):
        self.ma = f"GV{ma:02d}"
        self.ten = ten
        self.mon = mon_hoc[maxt[0]]
        self.tong = tin * 2 + cm + uu_tien[maxt[1]]
        if self.tong >= 18:
            self.kq = "TRUNG TUYEN"
        else:
            self.kq = "LOAI"

n = int(input())
ds = []
for i in range(1, n + 1):
    ten = input().strip()
    maxt = input().strip()
    tin = float(input().strip())
    cm = float(input().strip())
    ds.append(GiaoVien(i, ten, maxt, tin, cm))

ds.sort(key=lambda x: -x.tong)
for gv in ds:
    print(f"{gv.ma} {gv.ten} {gv.mon} {gv.tong:.1f} {gv.kq}")