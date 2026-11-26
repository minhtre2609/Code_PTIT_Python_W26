import gc
import re
import sys


def get_div_suffixes(k):
    t = k
    c2 = 0
    while t % 2 == 0:
        t //= 2
        c2 += 1
    c5 = 0
    while t % 5 == 0:
        t //= 5
        c5 += 1
    if t != 1:
        return None
    d = max(c2, c5)
    if d == 0 or d > 4:
        return None
    base = 10**d
    if base // k > 5:
        return None
    if d == 1:
        return tuple(f"{m}\n".encode() for m in range(0, 10, k)), True
    sufs = tuple(f"{m:0{d}d}\n".encode() for m in range(0, base, k))
    return sufs, False


def count_mod(bio, k, extra, is_pow2, init_ch=b""):
    read = bio.read
    buf = b""
    first = True
    if is_pow2:
        mask = k - 1
        cnt = len([1 for x in map(int, extra) if not (x & mask)]) if extra else 0
        while True:
            if first and init_ch:
                ch = init_ch
                first = False
            else:
                first = False
                ch = read(65536)
            if not ch:
                if buf:
                    cnt += len([1 for x in map(int, buf.split()) if not (x & mask)])
                return cnt
            if ch[-1] > 32:
                cut = ch.rfind(10)
                if cut == -1:
                    cut = max(ch.rfind(32), ch.rfind(9), ch.rfind(13))
                if cut == -1:
                    buf += ch
                    continue
                part = buf + ch[:cut] if buf else ch[:cut]
                buf = ch[cut + 1:]
            else:
                part = buf + ch if buf else ch
                buf = b""
            cnt += len([1 for x in map(int, part.split()) if not (x & mask)])

    cnt = len([1 for x in map(int, extra) if not (x % k)]) if extra else 0
    while True:
        if first and init_ch:
            ch = init_ch
            first = False
        else:
            first = False
            ch = read(65536)
        if not ch:
            if buf:
                cnt += len([1 for x in map(int, buf.split()) if not (x % k)])
            return cnt
        if ch[-1] > 32:
            cut = ch.rfind(10)
            if cut == -1:
                cut = max(ch.rfind(32), ch.rfind(9), ch.rfind(13))
            if cut == -1:
                buf += ch
                continue
            part = buf + ch[:cut] if buf else ch[:cut]
            buf = ch[cut + 1:]
        else:
            part = buf + ch if buf else ch
            buf = b""
        cnt += len([1 for x in map(int, part.split()) if not (x % k)])


def solve():
    gc.disable()
    bio = sys.stdin.buffer
    header = []
    while len(header) < 2:
        ln = bio.readline()
        if not ln:
            break
        header.extend(ln.split())
    if len(header) < 2:
        return
    n = int(header[0])
    k = int(header[1])
    if k == 1:
        sys.stdout.write(f"{n}\n")
        return

    extra = header[2:]
    is_pow2 = (k & (k - 1)) == 0
    suf_info = get_div_suffixes(k) if not extra else None
    if suf_info is not None:
        sufs, single_digit = suf_info
        read = bio.read
        buf = b""
        cnt = 0
        rx_zero = None if single_digit else re.compile(b"(?<=\\n)0(?=\\n)")
        while True:
            ch = read(1048576)
            if not ch:
                if buf:
                    blk = buf if buf.endswith(b"\n") else buf + b"\n"
                    for suf in sufs:
                        cnt += blk.count(suf)
                    if not single_digit:
                        padded = b"\n" + blk
                        if b"\n0\n" in padded:
                            cnt += len(rx_zero.findall(padded))
                sys.stdout.write(f"{cnt}\n")
                return
            if b" " in ch or b"\r" in ch or b"\t" in ch:
                cnt += count_mod(bio, k, [], is_pow2, buf + ch)
                sys.stdout.write(f"{cnt}\n")
                return
            if ch[-1] != 10:
                cut = ch.rfind(10)
                if cut == -1:
                    buf += ch
                    continue
                blk = buf + ch[:cut + 1] if buf else ch[:cut + 1]
                buf = ch[cut + 1:]
            else:
                blk = buf + ch if buf else ch
                buf = b""
            for suf in sufs:
                cnt += blk.count(suf)
            if not single_digit:
                padded = b"\n" + blk
                if b"\n0\n" in padded:
                    cnt += len(rx_zero.findall(padded))

    cnt = count_mod(bio, k, extra, is_pow2)
    sys.stdout.write(f"{cnt}\n")


solve()