import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for i in range(1, t + 1):
        s = d[i]
        sm = sum(int(c) for c in s)
        st = str(sm)
        if len(st) > 1 and st == st[::-1]:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()