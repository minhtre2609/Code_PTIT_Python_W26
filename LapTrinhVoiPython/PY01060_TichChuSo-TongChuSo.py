import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for k in range(1, t + 1):
        s = d[k]
        p = 1
        has = False
        s_odd = 0
        for i, c in enumerate(s):
            v = int(c)
            if i % 2 == 0:
                if v != 0:
                    p *= v
                    has = True
            else:
                s_odd += v
        if not has:
            p = 0
        print(f'{p} {s_odd}')

if __name__ == '__main__':
    solve()