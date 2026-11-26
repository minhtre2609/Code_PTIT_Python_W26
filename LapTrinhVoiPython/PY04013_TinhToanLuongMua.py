def to_min(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m

n = int(input())
stations = {}
for _ in range(n):
    name = input().strip()
    t1 = to_min(input().strip())
    t2 = to_min(input().strip())
    rain = float(input())
    if name not in stations:
        stations[name] = [0.0, 0]
    stations[name][0] += rain
    stations[name][1] += t2 - t1

for idx, (name, val) in enumerate(stations.items(), 1):
    avg = val[0] * 60 / val[1]
    print(f"T{idx:02d} {name} {avg:.2f}")