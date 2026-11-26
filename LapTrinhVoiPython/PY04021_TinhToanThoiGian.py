class GameThu:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        h1, m1 = map(int, vao.split(":"))
        h2, m2 = map(int, ra.split(":"))
        self.phut = (h2 * 60 + m2) - (h1 * 60 + m1)

n = int(input())
ds = []
for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    vao = input().strip()
    ra = input().strip()
    ds.append(GameThu(ma, ten, vao, ra))

ds.sort(key=lambda x: -x.phut)
for gt in ds:
    print(f"{gt.ma} {gt.ten} {gt.phut // 60} gio {gt.phut % 60} phut")