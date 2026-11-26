import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    idx = 1
    for _ in range(t):
        n = int(d[idx])
        k = int(d[idx + 1])
        idx += 2
        low = k & -k
        pos = low.bit_length() - 1
        print(chr(65 + pos))

if __name__ == '__main__':
    solve()