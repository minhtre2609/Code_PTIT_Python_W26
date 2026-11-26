import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for k in range(1, t + 1):
        s = list(d[k])
        n = len(s)
        i = n - 2
        while i >= 0 and s[i] <= s[i + 1]:
            i -= 1
        if i < 0:
            print(-1)
            continue
        mx = '-1'
        idx = -1
        for j in range(i + 1, n):
            if s[j] < s[i]:
                if s[j] > mx:
                    mx = s[j]
                    idx = j
        if idx == -1 or (i == 0 and s[idx] == '0'):
            print(-1)
        else:
            s[i], s[idx] = s[idx], s[i]
            print(''.join(s))

if __name__ == '__main__':
    solve()