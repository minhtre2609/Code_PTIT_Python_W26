from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        g = gcd(tu, mau)
        self.tu = tu // g
        self.mau = mau // g

    def __str__(self):
        return f"{self.tu}/{self.mau}"

a, b = map(int, input().split())
print(PhanSo(a, b))