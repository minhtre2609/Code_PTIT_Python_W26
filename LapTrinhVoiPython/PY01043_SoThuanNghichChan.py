import sys
from itertools import product

def generate_numbers():
    nums = []
    for half_len in (1, 2, 3):
        for d1 in '2468':
            for rest in product('02468', repeat=half_len - 1):
                half = d1 + ''.join(rest)
                full = half + half[::-1]
                nums.append(int(full))
    nums.sort()
    return nums

ALL_NUMS = generate_numbers()

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        res = [str(x) for x in ALL_NUMS if x < n]
        out.append(' '.join(res))
    sys.stdout.write('\n'.join(out) + '\n')

solve()