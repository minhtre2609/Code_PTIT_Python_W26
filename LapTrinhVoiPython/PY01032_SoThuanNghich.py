import sys

def is_pal(x, k):
    t = []
    while x > 0:
        t.append(x % k)
        x //= k
    return t == t[::-1]

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    a = int(d[0])
    b = int(d[1])
    m = int(d[2])
    
    p = [0]
    for l in range(1, 22):
        h = (l + 1) // 2
        for v in range(1 << (h - 1), 1 << h):
            s = bin(v)[2:]
            if l % 2 == 1:
                ps = s + s[:-1][::-1]
            else:
                ps = s + s[::-1]
            val = int(ps, 2)
            if val <= 2000000:
                p.append(val)
    p.sort()
    
    ans = 0
    for x in p:
        if x < a:
            continue
        if x > b:
            break
        ok = True
        limit = min(m, x)
        for k in range(3, limit + 1):
            if not is_pal(x, k):
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()