import sys

pr = [True] * 505
pr[0] = pr[1] = False
for i in range(2, 25):
    if pr[i]:
        for j in range(i * i, 505, i):
            pr[j] = False

p_dig = {'2', '3', '5', '7'}

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for k in range(1, t + 1):
        s = d[k]
        ok = True
        for i, c in enumerate(s):
            if pr[i] != (c in p_dig):
                ok = False
                break
        if ok:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()