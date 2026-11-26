from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        g = gcd(tu, mau)
        self.tu = tu // g
        self.mau = mau // g

    def add(self, other):
        return PhanSo(self.tu * other.mau + other.tu * self.mau, self.mau * other.mau)

    def __str__(self):
        return f"{self.tu}/{self.mau}"

a, b, c, d = map(int, input().split())
p = PhanSo(a, b)
q = PhanSo(c, d)
print(p.add(q))