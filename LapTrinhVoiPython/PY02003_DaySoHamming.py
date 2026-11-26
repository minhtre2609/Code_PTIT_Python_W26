import sys

def solve():
    MAX = 10**18
    nums = []
    p2 = 1
    while p2 <= MAX:
        p3 = p2
        while p3 <= MAX:
            p5 = p3
            while p5 <= MAX:
                nums.append(p5)
                p5 *= 5
            p3 *= 3
        p2 *= 2
    nums.sort()
    pos = {v: i + 1 for i, v in enumerate(nums)}
    
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        p = pos.get(n)
        out.append(str(p) if p else "Not in sequence")
    sys.stdout.write("\n".join(out) + "\n")

solve()