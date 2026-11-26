class ThiSinh:
    def __init__(self, ma, ten, lt, th):
        self.ma = f"TS0{ma}"
        self.ten = ten
        if lt > 10:
            lt /= 10
        if th > 10:
            th /= 10
        self.tb = (lt + th) / 2
        if self.tb < 5:
            self.xl = "TRUOT"
        elif self.tb < 8:
            self.xl = "CAN NHAC"
        elif self.tb <= 9.5:
            self.xl = "DAT"
        else:
            self.xl = "XUAT SAC"

n = int(input())
ds = []
for i in range(1, n + 1):
    ten = input().strip()
    lt = float(input().strip())
    th = float(input().strip())
    ds.append(ThiSinh(i, ten, lt, th))

ds.sort(key=lambda x: -x.tb)
for ts in ds:
    print(f"{ts.ma} {ts.ten} {ts.tb:.2f} {ts.xl}")