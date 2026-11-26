class MonThi:
    def __init__(self, ma, ten, ht):
        self.ma = ma
        self.ten = ten
        self.ht = ht

n = int(input())
ds = []
for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    ht = input().strip()
    ds.append(MonThi(ma, ten, ht))

ds.sort(key=lambda x: x.ma)
for m in ds:
    print(m.ma, m.ten, m.ht)