import sys

def solve():
    it = sys.stdin.readline
    t_str = it()
    if not t_str:
        return
    t = int(t_str)
    e = -10**9
    for _ in range(t):
        it()
        s = it()
        x = e
        y = e
        z = e
        if len(s) < 10000:
            for v in map(int, s.split()):
                if v <= z:
                    continue
                if v >= x:
                    z, y, x = y, x, v
                elif v >= y:
                    z, y = y, v
                else:
                    z = v
        else:
            m1 = len(s) // 3
            while m1 > 0 and s[m1] != ' ':
                m1 -= 1
            m2 = (2 * len(s)) // 3
            while m2 > 0 and s[m2] != ' ':
                m2 -= 1
            for chunk in (s[:m1], s[m1+1:m2], s[m2+1:]):
                for v in map(int, chunk.split()):
                    if v <= z:
                        continue
                    if v >= x:
                        z, y, x = y, x, v
                    elif v >= y:
                        z, y = y, v
                    else:
                        z = v
        print(x + y + z)

if __name__ == '__main__':
    solve()