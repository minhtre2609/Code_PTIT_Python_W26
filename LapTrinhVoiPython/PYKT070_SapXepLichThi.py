mon = {}
with open('MONTHI.in', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
n_mon = int(lines[0])
idx = 1
for _ in range(n_mon):
    ma_m = lines[idx]
    ten_m = lines[idx + 1]
    idx += 3
    mon[ma_m] = ten_m

ca = {}
with open('CATHI.in', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
n_ca = int(lines[0])
idx = 1
for i in range(1, n_ca + 1):
    ma_c = f"C{i:03d}"
    ngay = lines[idx]
    gio = lines[idx + 1]
    phong = lines[idx + 2]
    idx += 3
    d, m, y = map(int, ngay.split('/'))
    hh, mm = map(int, gio.split(':'))
    ca[ma_c] = (y, m, d, hh, mm, ngay, gio, phong)

lich = []
with open('LICHTHI.in', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
n_lich = int(lines[0])
for i in range(1, n_lich + 1):
    parts = lines[i].split()
    ma_c = parts[0]
    ma_m = parts[1]
    nhom = parts[2]
    so_sv = parts[3]
    
    y, m, d, hh, mm, ngay, gio, phong = ca[ma_c]
    key = (y, m, d, hh, mm, ma_c)
    lich.append((key, ngay, gio, phong, mon[ma_m], nhom, so_sv))

lich.sort(key=lambda x: x[0])

for x in lich:
    print(f"{x[1]} {x[2]} {x[3]} {x[4]} {x[5]} {x[6]}")