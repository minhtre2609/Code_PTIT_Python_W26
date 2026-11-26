import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    q = int(data[1])
    diff = [0] * (n + 2)
    idx = 2
    for _ in range(q):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        diff[x] ^= 1
        diff[y + 1] ^= 1
        
    cur = 0
    ans = []
    for i in range(1, n + 1):
        cur ^= diff[i]
        ans.append(str(cur))
        
    print(' '.join(ans))