import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    it = iter(tokens)
    t = int(next(it))
    for _ in range(t):
        p = next(it)
        q = next(it)
        x1 = next(it)
        x2 = next(it)
        
        d_min = min(p, q)
        d_max = max(p, q)
        
        min_x1 = int(x1.replace(d_max, d_min))
        min_x2 = int(x2.replace(d_max, d_min))
        min_sum = min_x1 + min_x2
        
        max_x1 = int(x1.replace(d_min, d_max))
        max_x2 = int(x2.replace(d_min, d_max))
        max_sum = max_x1 + max_x2
        
        print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    solve()
