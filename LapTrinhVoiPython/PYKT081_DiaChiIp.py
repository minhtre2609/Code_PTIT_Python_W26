t = int(input())
for _ in range(t):
    parts = input().strip().split(".")
    ok = len(parts) == 4
    if ok:
        for p in parts:
            if not p or not all("0" <= c <= "9" for c in p) or int(p) > 255:
                ok = False
                break
    print("YES" if ok else "NO")