class KhachHang:
    def __init__(self, ma, ten, cu, moi):
        self.ma = f"KH{ma:02d}"
        self.ten = ten
        so = moi - cu
        if so <= 50:
            tien = so * 100 * 1.02
        elif so <= 100:
            tien = (50 * 100 + (so - 50) * 150) * 1.03
        else:
            tien = (50 * 100 + 50 * 150 + (so - 100) * 200) * 1.05
        self.tien = round(tien)

n = int(input())
ds = []
for i in range(1, n + 1):
    ten = input().strip()
    cu = int(input())
    moi = int(input())
    ds.append(KhachHang(i, ten, cu, moi))

ds.sort(key=lambda x: -x.tien)
for kh in ds:
    print(kh.ma, kh.ten, kh.tien)