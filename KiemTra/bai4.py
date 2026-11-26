class Phim:
    def __init__(self, ma_phim, ten_tl, ngay, ten_phim, so_tap):
        self.ma_phim = ma_phim
        self.ten_tl = ten_tl
        self.ngay = ngay
        self.ten_phim = ten_phim
        self.so_tap = so_tap
        d, m, y = map(int, ngay.split("/"))
        self.d = d
        self.m = m
        self.y = y
    def __str__(self):
        return f"{self.ma_phim} {self.ten_tl} {self.ngay} {self.ten_phim} {self.so_tap}"

n, m = map(int, input().split())

the_loai = {}
for i in range(1, n + 1):
    ma_tl = f"TL{i:03d}"
    the_loai[ma_tl] = input().strip()

ds_phim = []
for i in range(1, m + 1):
    ma_phim = f"P{i:03d}"
    ma_tl = input().strip()
    ngay = input().strip()
    ten_phim = input().strip()
    so_tap = int(input().strip())
    ds_phim.append(Phim(ma_phim, the_loai[ma_tl], ngay, ten_phim, so_tap))

ds_phim.sort(key=lambda x: (x.y, x.m, x.d, x.ten_phim, -x.so_tap))

for p in ds_phim:
    print(p)
