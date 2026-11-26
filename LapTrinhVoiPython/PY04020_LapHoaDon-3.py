class HoaDon:
    def __init__(self, ma, ten, sl, gia, ck):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.ck = ck
        self.tong = sl * gia - ck

n = int(input())
ds = []
for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    sl = int(input().strip())
    gia = int(input().strip())
    ck = int(input().strip())
    ds.append(HoaDon(ma, ten, sl, gia, ck))

ds.sort(key=lambda x: -x.tong)
for hd in ds:
    print(hd.ma, hd.ten, hd.sl, hd.gia, hd.ck, hd.tong)