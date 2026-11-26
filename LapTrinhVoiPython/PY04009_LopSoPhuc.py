class SoPhuc:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, other):
        return SoPhuc(self.r + other.r, self.i + other.i)

    def mul(self, other):
        return SoPhuc(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        return f"{self.r} - {-self.i}i"

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    z1 = SoPhuc(a, b)
    z2 = SoPhuc(c, d)
    s = z1.add(z2)
    print(f"{s.mul(z1)}, {s.mul(s)}")