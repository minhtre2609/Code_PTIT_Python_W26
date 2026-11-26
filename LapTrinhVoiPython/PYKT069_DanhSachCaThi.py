with open('CATHI.in', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

n = int(lines[0])
ds = []
idx = 1
for i in range(1, n + 1):
    ma = f"C{i:03d}"
    ngay = lines[idx]
    gio = lines[idx + 1]
    phong = lines[idx + 2]
    idx += 3
    
    d, m, y = map(int, ngay.split('/'))
    hh, mm = map(int, gio.split(':'))
    
    key = (y, m, d, hh, mm, ma)
    ds.append((key, ma, ngay, gio, phong))

ds.sort(key=lambda x: x[0])

for x in ds:
    print(f"{x[1]} {x[2]} {x[3]} {x[4]}")