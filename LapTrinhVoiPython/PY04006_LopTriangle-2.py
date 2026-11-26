import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.a = p1.dist(p2)
        self.b = p2.dist(p3)
        self.c = p3.dist(p1)

    def area(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "INVALID"
        s = (self.a + self.b + self.c) / 2
        val = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return f"{val:.2f}"

t = int(input())
vals = []
while len(vals) < 6 * t:
    vals.extend(map(float, input().split()))
for i in range(t):
    x1, y1, x2, y2, x3, y3 = vals[6 * i : 6 * i + 6]
    tri = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    print(tri.area())