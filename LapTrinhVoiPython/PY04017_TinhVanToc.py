class CuaRo:
    def __init__(self, ten, donvi, dich):
        self.ten = ten
        self.donvi = donvi
        ma = ""
        for w in donvi.split():
            ma += w[0].upper()
        for w in ten.split():
            ma += w[0].upper()
        self.ma = ma
        h, m = map(int, dich.split(":"))
        self.tg = (h - 6) + m / 60
        self.vt = round(120 / self.tg)

n = int(input())
ds = []
for _ in range(n):
    ten = input().strip()
    donvi = input().strip()
    dich = input().strip()
    ds.append(CuaRo(ten, donvi, dich))

ds.sort(key=lambda x: x.tg)
for c in ds:
    print(f"{c.ma} {c.ten} {c.donvi} {c.vt} Km/h")