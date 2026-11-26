import gc
import heapq
import re
import sys

try:
    re.compile(b"a{1,2}+")
    HAS_POSS = True
except re.error:
    HAS_POSS = False

SHORT_POSS = [re.compile(f" [0-9]{{1,{k}}}+(?= )".encode()) for k in range(1, 12)] if HAS_POSS else []
POS_EXACT = [re.compile(b" \\d(?= )" if k == 1 else f" [1-9]\\d{{{k - 1}}}(?= )".encode()) for k in range(1, 12)]
NEG_ALL = re.compile(b" -\\d+(?= )")
NEG_NINE = re.compile(b" -1\\d{8,}(?= )")


def same_len_le_rx(s_num):
    L = len(s_num)

    def rec(idx):
        if idx == L - 1:
            d = s_num[idx]
            return d if d == "0" else f"[0-{d}]"
        d = int(s_num[idx])
        lo = 1 if (idx == 0 and L > 1) else 0
        rem = L - 1 - idx
        tail = r"\d" if rem == 1 else f"\\d{{{rem}}}"
        parts = []
        if d > lo:
            hi = d - 1
            rng_s = str(lo) if lo == hi else f"[{lo}-{hi}]"
            parts.append(f"{rng_s}{tail}")
        parts.append(f"{d}{rec(idx + 1)}")
        return "(?:" + "|".join(parts) + ")" if len(parts) > 1 else parts[0]

    return rec(0)


def same_len_ge_rx(s_num):
    L = len(s_num)

    def rec(idx):
        if idx == L - 1:
            d = s_num[idx]
            return "9" if d == "9" else f"[{d}-9]"
        d = int(s_num[idx])
        rem = L - 1 - idx
        tail = r"\d" if rem == 1 else f"\\d{{{rem}}}"
        parts = []
        if d < 9:
            lo = d + 1
            rng_s = "9" if lo == 9 else f"[{lo}-9]"
            parts.append(f"{rng_s}{tail}")
        parts.append(f"{d}{rec(idx + 1)}")
        return "(?:" + "|".join(parts) + ")" if len(parts) > 1 else parts[0]

    return rec(0)


def solve_fast_line(raw):
    if b"\t" in raw:
        raw = raw.replace(b"\t", b" ")
    s = b" " + raw.strip() + b" "
    del raw
    L = len(s)
    samp = []
    step = L // 32
    if step >= 512:
        win = min(1024, step)
        for ki in range(32):
            st = ki * step
            en = st + win
            if st > 0:
                while st < en and s[st] > 32:
                    st += 1
            if en < L:
                while en > st and s[en - 1] > 32:
                    en -= 1
            if st < en:
                samp.extend(map(int, s[st:en].split()))
    if len(samp) < 3:
        return sum(heapq.nsmallest(3, map(int, s.split())))
    m3 = heapq.nsmallest(3, samp)[2]
    target = m3 - 1
    if target < 0:
        st_s = str(-target)
        lt = len(st_s)
        found = []
        if lt == 8:
            found.extend(map(int, NEG_NINE.findall(s)))
        elif lt < 8:
            found.extend(map(int, re.findall(b" -\\d{" + str(lt + 1).encode() + b",}(?= )", s)))
        if len(found) < 3:
            found.extend(map(int, re.findall(b" -" + same_len_ge_rx(st_s).encode() + b"(?= )", s)))
    else:
        found = [int(x) for x in NEG_ALL.findall(s)] if b"-" in s else []
        if len(found) < 3:
            st_s = str(target)
            lt = len(st_s)
            if lt >= 2:
                if HAS_POSS and lt - 2 < len(SHORT_POSS):
                    found.extend(map(int, SHORT_POSS[lt - 2].findall(s)))
                elif lt <= 5:
                    for dk in range(lt - 1):
                        m = POS_EXACT[dk].findall(s)
                        if m:
                            found.extend(map(int, m))
                            if len(found) >= 3:
                                break
                else:
                    short_pat = f" (?:0|[1-9]\\d{{0,{lt - 2}}})(?= )".encode()
                    found.extend(map(int, re.findall(short_pat, s)))
            if len(found) < 3:
                found.extend(map(int, re.findall(b" " + same_len_le_rx(st_s).encode() + b"(?= )", s)))
    if len(found) >= 3:
        return sum(heapq.nsmallest(3, found))
    return sum(found) + m3 * (3 - len(found))


def read_nonempty(bio):
    while True:
        ln = bio.readline()
        if not ln or ln.strip():
            return ln


def iter_n(bio, initial_toks, n):
    yield from map(int, initial_toks)
    seen = len(initial_toks)
    while seen < n:
        ln = read_nonempty(bio)
        if not ln:
            break
        toks = ln.split()
        seen += len(toks)
        yield from map(int, toks)


def solve():
    gc.disable()
    bio = sys.stdin.buffer
    first = read_nonempty(bio)
    if not first:
        return
    t = int(first.split()[0])
    out = []
    nsmallest = heapq.nsmallest
    for _ in range(t):
        nline = read_nonempty(bio)
        if not nline:
            break
        ntoks = nline.split()
        n = int(ntoks[0])
        if len(ntoks) > 1:
            out.append(str(sum(nsmallest(3, iter_n(bio, ntoks[1:], n)))))
        else:
            line = read_nonempty(bio)
            if not line:
                break
            if len(line) >= 150000 and line.count(b" ") >= n - 1:
                out.append(str(solve_fast_line(line)))
            else:
                toks = line.split()
                if len(toks) >= n:
                    out.append(str(sum(nsmallest(3, map(int, toks)))))
                else:
                    out.append(str(sum(nsmallest(3, iter_n(bio, toks, n)))))
    sys.stdout.write("\n".join(out) + "\n")


solve()