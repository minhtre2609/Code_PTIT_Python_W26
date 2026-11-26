def band(c):
    if c >= 39:
        return 9.0
    if c >= 37:
        return 8.5
    if c >= 35:
        return 8.0
    if c >= 33:
        return 7.5
    if c >= 30:
        return 7.0
    if c >= 27:
        return 6.5
    if c >= 23:
        return 6.0
    if c >= 20:
        return 5.5
    if c >= 16:
        return 5.0
    if c >= 13:
        return 4.5
    if c >= 10:
        return 4.0
    if c >= 7:
        return 3.5
    if c >= 5:
        return 3.0
    if c >= 3:
        return 2.5
    return 1.0

t = int(input())
for _ in range(t):
    parts = input().split()
    r = band(int(parts[0]))
    l = band(int(parts[1]))
    s = float(parts[2])
    w = float(parts[3])
    t2 = round((r + l + s + w) * 2)
    whole, rem = divmod(t2, 8)
    if rem < 2:
        ans = float(whole)
    elif rem <= 5:
        ans = whole + 0.5
    else:
        ans = float(whole + 1)
    print(f"{ans:.1f}")