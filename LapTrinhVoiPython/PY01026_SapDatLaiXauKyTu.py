import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    idx = 1
    for i in range(1, t + 1):
        s1 = d[idx]
        s2 = d[idx + 1]
        idx += 2
        if sorted(s1) == sorted(s2):
            print(f"Test {i}: YES")
        else:
            print(f"Test {i}: NO")

if __name__ == '__main__':
    solve()