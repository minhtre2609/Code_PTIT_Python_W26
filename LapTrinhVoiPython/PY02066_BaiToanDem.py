import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    nums = set(int(x) for x in raw[1:1 + n])
    max_val = max(nums)
    missing = [x for x in range(1, max_val + 1) if x not in nums]
    if not missing:
        print("Excellent!")
        return
    for x in missing:
        print(x)

if __name__ == '__main__':
    solve()