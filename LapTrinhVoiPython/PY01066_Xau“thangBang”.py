import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for k in range(1, t + 1):
        s = d[k]
        r = s[::-1]
        n = len(s)
        ok = True
        for i in range(1, n):
            if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
                ok = False
                break
        if ok:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()