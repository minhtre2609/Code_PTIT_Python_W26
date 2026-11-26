from datetime import datetime

gia = {'1': 25, '2': 34, '3': 50, '4': 80}

class KhachHang:
    def __init__(self, ma, ten, phong, nhan, tra, dv):
        self.ma = f"KH{ma:02d}"
        self.ten = ten
        self.phong = phong
        d1 = datetime.strptime(nhan, "%d/%m/%Y")
        d2 = datetime.strptime(tra, "%d/%m/%Y")
        self.ngay = (d2 - d1).days + 1
        self.tien = self.ngay * gia[phong[0]] + dv

n = int(input())
ds = []
for i in range(1, n + 1):
    ten = input().strip()
    phong = input().strip()
    nhan = input().strip()
    tra = input().strip()
    dv = int(input().strip())
    ds.append(KhachHang(i, ten, phong, nhan, tra, dv))

ds.sort(key=lambda x: -x.tien)
for kh in ds:
    print(kh.ma, kh.ten, kh.phong, kh.ngay, kh.tien)