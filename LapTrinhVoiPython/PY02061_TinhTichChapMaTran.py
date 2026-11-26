import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    ptr = 0
    t = int(raw[ptr])
    ptr += 1
    out = []
    for _ in range(t):
        n = int(raw[ptr])
        m = int(raw[ptr + 1])
        ptr += 2
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            row_vals = [int(x) for x in raw[ptr:ptr + m]]
            ptr += m
            row_sum = 0
            for j in range(m):
                row_sum += row_vals[j]
                pref[i + 1][j + 1] = pref[i][j + 1] + row_sum
        kernel = []
        for _ in range(3):
            kernel.append([int(x) for x in raw[ptr:ptr + 3]])
            ptr += 3
        total = 0
        r_len = n - 2
        c_len = m - 2
        for u in range(3):
            r1 = u
            r2 = u + r_len
            for v in range(3):
                c1 = v
                c2 = v + c_len
                sub_sum = pref[r2][c2] - pref[r1][c2] - pref[r2][c1] + pref[r1][c1]
                total += sub_sum * kernel[u][v]
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()