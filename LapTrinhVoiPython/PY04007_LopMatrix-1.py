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

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    mat = Matrix(n, m, a)
    for row in mat.mul_transpose():
        print(*row)