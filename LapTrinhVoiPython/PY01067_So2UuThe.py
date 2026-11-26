import sys
from collections import deque

def solve():
    res = []
    q = deque(['1', '2'])
    while len(res) < 1000:
        s = q.popleft()
        if s.count('2') > len(s) / 2:
            res.append(s)
        q.append(s + '0')
        q.append(s + '1')
        q.append(s + '2')

    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for k in range(1, t + 1):
        n = int(d[k])
        print(' '.join(res[:n]))

if __name__ == '__main__':
    solve()