import sys

def solve():
    lines = sys.stdin
    first_line = lines.readline()
    while first_line and not first_line.strip():
        first_line = lines.readline()
    if not first_line:
        return
    t = int(first_line.strip())
    out = []
    for _ in range(t):
        dim_line = lines.readline()
        while dim_line and not dim_line.strip():
            dim_line = lines.readline()
        if not dim_line:
            break
        m, n = map(int, dim_line.split())
        if m == 0 or n == 0:
            out.append("0")
            continue
        prev_row = [0] * n
        total = 0
        for _ in range(m):
            curr_row = []
            while len(curr_row) < n:
                curr_row.extend(int(x) for x in lines.readline().split())
            total += curr_row[0] + curr_row[-1]
            for c in range(n):
                if curr_row[c] > 0:
                    total += 2
                total += abs(curr_row[c] - prev_row[c])
            for c in range(n - 1):
                total += abs(curr_row[c] - curr_row[c + 1])
            prev_row = curr_row
        total += sum(prev_row)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()