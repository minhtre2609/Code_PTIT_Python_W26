import sys

lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
if lines:
    n, m = map(int, lines[0].split())
    the_loai = {}
    for i in range(1, n + 1):
        the_loai[f"TL{i:03d}"] = lines[i]
        
    phim = []
    idx = n + 1
    for i in range(1, m + 1):
        ma_p = f"P{i:03d}"
        ma_tl = lines[idx]
        ngay = lines[idx + 1]
        ten = lines[idx + 2]
        so_tap = int(lines[idx + 3])
        idx += 4
        
        d, mon, y = map(int, ngay.split('/'))
        key = (y, mon, d, ten, -so_tap)
        phim.append((key, ma_p, the_loai[ma_tl], ngay, ten, so_tap))
        
    phim.sort(key=lambda x: x[0])
    
    for p in phim:
        print(f"{p[1]} {p[2]} {p[3]} {p[4]} {p[5]}")