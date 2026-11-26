class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a

    def mul_transpose(self):
        res = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                s = 0
                for k in range(self.m):
                    s += self.a[i][k] * self.a[j][k]
                row.append(s)
            res.append(row)
        return res

def next_ints():
    while True:
        s = input().split()
        if s:
            return list(map(int, s))

t = next_ints()[0]
for _ in range(t):
    n, m = next_ints()
    a = []
    for _ in range(n):
        row = []
        while len(row) < m:
            row.extend(next_ints())
        a.append(row)
    mat = Matrix(n, m, a)
    for row in mat.mul_transpose():
        print(*row)