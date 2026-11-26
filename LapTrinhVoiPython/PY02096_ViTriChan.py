import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    m = int(data[0])
    d = int(data[1])
    a_str = data[2]
    b_str = data[3]
    mod = 1000000007
    length = len(a_str)
    a_dig = [int(c) for c in a_str]
    b_dig = [int(c) for c in b_str]
    w = [pow(10, length - 1 - i, m) for i in range(length)]
    base_odd = 0
    for i in range(1, length, 2):
        base_odd = (base_odd + d * w[i]) % m

    if a_dig == b_dig:
        rem = base_odd
        for i in range(length):
            if i % 2 == 1:
                if a_dig[i] != d:
                    sys.stdout.write('0\n')
                    return
            else:
                if a_dig[i] == d:
                    sys.stdout.write('0\n')
                    return
                rem = (rem + a_dig[i] * w[i]) % m
        sys.stdout.write(('1\n' if rem == 0 else '0\n'))
        return

    b_bits = 96
    b_bytes = 12
    mask_m = (1 << (m * b_bits)) - 1
    slot_mask = (1 << b_bits) - 1

    lcp = 0
    rem_pref = base_odd
    while lcp < length and a_dig[lcp] == b_dig[lcp]:
        c = a_dig[lcp]
        if lcp % 2 == 1:
            if c != d:
                sys.stdout.write('0\n')
                return
        else:
            if c == d:
                sys.stdout.write('0\n')
                return
            rem_pref = (rem_pref + c * w[lcp]) % m
        lcp += 1

    dp = 0
    ok_a = False
    ok_b = False
    rem_a = 0
    rem_b = 0

    i = lcp
    wi = w[i]
    if i % 2 == 1:
        if a_dig[i] < d < b_dig[i]:
            dp += 1 << (rem_pref * b_bits)
        if a_dig[i] == d:
            ok_a = True
            rem_a = rem_pref
        if b_dig[i] == d:
            ok_b = True
            rem_b = rem_pref
    else:
        for c in range(a_dig[i] + 1, b_dig[i]):
            if c != d:
                dp += 1 << (((rem_pref + c * wi) % m) * b_bits)
        if a_dig[i] != d:
            ok_a = True
            rem_a = (rem_pref + a_dig[i] * wi) % m
        if b_dig[i] != d:
            ok_b = True
            rem_b = (rem_pref + b_dig[i] * wi) % m

    step_cnt = 0
    for i in range(lcp + 1, length):
        wi = w[i]
        if i % 2 == 1:
            if ok_a:
                if d > a_dig[i]:
                    dp += 1 << (rem_a * b_bits)
                    ok_a = False
                elif d < a_dig[i]:
                    ok_a = False
            if ok_b:
                if d < b_dig[i]:
                    dp += 1 << (rem_b * b_bits)
                    ok_b = False
                elif d > b_dig[i]:
                    ok_b = False
        else:
            if dp:
                ndp = 0
                for c in range(10):
                    if c != d:
                        ndp += dp << (((c * wi) % m) * b_bits)
                dp = (ndp & mask_m) + (ndp >> (m * b_bits))
                step_cnt += 1
            if ok_a:
                for c in range(a_dig[i] + 1, 10):
                    if c != d:
                        dp += 1 << (((rem_a + c * wi) % m) * b_bits)
                if a_dig[i] == d:
                    ok_a = False
                else:
                    rem_a = (rem_a + a_dig[i] * wi) % m
            if ok_b:
                for c in range(0, b_dig[i]):
                    if c != d:
                        dp += 1 << (((rem_b + c * wi) % m) * b_bits)
                if b_dig[i] == d:
                    ok_b = False
                else:
                    rem_b = (rem_b + b_dig[i] * wi) % m
            if dp and step_cnt >= 18:
                step_cnt = 0
                dp = (dp & mask_m) + (dp >> (m * b_bits))
                raw = dp.to_bytes(m * b_bytes, 'little')
                from_b = int.from_bytes
                chunks = [(from_b(raw[j:j + b_bytes], 'little') % mod).to_bytes(b_bytes, 'little') for j in range(0, m * b_bytes, b_bytes)]
                dp = from_b(b''.join(chunks), 'little')

    dp = (dp & mask_m) + (dp >> (m * b_bits))
    ans = (dp & slot_mask) % mod
    if ok_a and rem_a == 0:
        ans = (ans + 1) % mod
    if ok_b and rem_b == 0:
        ans = (ans + 1) % mod
    sys.stdout.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()