import sys

def solve_system(n, mat):
    eps = 1e-9
    for col in range(n):
        pivot = col
        max_val = abs(mat[col][col])
        for r in range(col + 1, n):
            if abs(mat[r][col]) > max_val:
                max_val = abs(mat[r][col])
                pivot = r
        if max_val < eps:
            return None
        if pivot != col:
            mat[col], mat[pivot] = mat[pivot], mat[col]
        div = mat[col][col]
        for j in range(col, n + 1):
            mat[col][j] /= div
        for r in range(n):
            if r != col:
                factor = mat[r][col]
                if abs(factor) > eps:
                    for j in range(col, n + 1):
                        mat[r][j] -= factor * mat[col][j]
    ans = []
    for i in range(n):
        v = mat[i][n]
        if abs(v) < 1e-9:
            v = 0.0
        ans.append(f"{v:.3f}")
    return " ".join(ans)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        A = []
        for _ in range(n):
            A.append([float(x) for x in data[idx:idx + n]])
            idx += n
        B = [float(x) for x in data[idx:idx + n]]
        idx += n
        for i in range(n):
            A[i].append(B[i])
        res = solve_system(n, A)
        out.append("-1" if res is None else res)
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()