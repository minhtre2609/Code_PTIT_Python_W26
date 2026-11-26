with open("DATA.in", "r") as f:
    toks = f.read().split()

if toks:
    t = int(toks[0])
    idx = 1
    tables = {
        4: {f"{v:02b}": f"{v:X}" for v in range(4)},
        8: {f"{v:03b}": f"{v:X}" for v in range(8)},
        16: {f"{v:04b}": f"{v:X}" for v in range(16)},
    }
    ks = {4: 2, 8: 3, 16: 4}
    out = []
    for _ in range(t):
        b = int(toks[idx])
        s = toks[idx + 1]
        idx += 2
        if b == 2:
            out.append(s.lstrip("0") or "0")
            continue
        k = ks[b]
        mp = tables[b]
        rem = len(s) % k
        if rem:
            s = "0" * (k - rem) + s
        res = "".join(mp[s[i : i + k]] for i in range(0, len(s), k)).lstrip("0")
        out.append(res or "0")
    print("\n".join(out))