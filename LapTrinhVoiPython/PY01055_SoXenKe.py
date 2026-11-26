import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for k in range(1, t + 1):
        s = d[k]
        n = len(s)
        if n % 2 == 0 or s[0] == s[1]:
            print('NO')
            continue
        ok = True
        for i in range(2, n, 2):
            if s[i] != s[0]:
                ok = False
                break
        if ok:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()