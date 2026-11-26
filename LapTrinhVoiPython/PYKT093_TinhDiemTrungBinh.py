import math

def chuan_hoa(name):
    return ' '.join(w.capitalize() for w in name.strip().split())

n = int(input())
ds = []
for i in range(1, n + 1):
    ma = f"SV{i:02d}"
    ten = chuan_hoa(input())
    d1 = int(input().strip())
    d2 = int(input().strip())
    d3 = int(input().strip())
    
    tb = math.ceil(((d1 * 3 + d2 * 3 + d3 * 2) / 8) * 100) / 100
    ds.append([ma, ten, tb])

ds.sort(key=lambda x: (-x[2], x[0]))

rank = 1
for i in range(n):
    if i > 0 and ds[i][2] < ds[i - 1][2]:
        rank = i + 1
    print(f"{ds[i][0]} {ds[i][1]} {ds[i][2]:.2f} {rank}")