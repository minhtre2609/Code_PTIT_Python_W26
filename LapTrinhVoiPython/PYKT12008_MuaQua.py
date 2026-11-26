import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    if k > m:
        sys.stdout.write('-1\n')
        return
    costs = [int(x) for x in data[3:3 + n]]
    idx = 3 + n
    a_cnt = int(data[idx])
    idx += 1
    a_items = [int(x) - 1 for x in data[idx:idx + a_cnt]]
    idx += a_cnt
    b_cnt = int(data[idx])
    idx += 1
    b_items = [int(x) - 1 for x in data[idx:idx + b_cnt]]

    mask = [0] * n
    for x in a_items:
        mask[x] |= 1
    for x in b_items:
        mask[x] |= 2

    g = [[], [], [], []]
    for i in range(n):
        g[mask[i]].append(costs[i])
    for i in range(4):
        g[i].sort()

    pref = [[0] * (len(g[i]) + 1) for i in range(4)]
    for i in range(4):
        s = 0
        arr = g[i]
        p = pref[i]
        for j, v in enumerate(arr):
            s += v
            p[j + 1] = s

    min_x = max(0, k - len(g[1]), k - len(g[2]), m - len(g[0]) - len(g[1]) - len(g[2]))
    max_x = min(m, len(g[3]))
    if min_x > max_x:
        sys.stdout.write('-1\n')
        return

    used = []
    unused = []
    sum_used = 0

    def add_pool(val):
        nonlocal sum_used
        if used and val < -used[0]:
            top = -heappop(used)
            sum_used += val - top
            heappush(used, -val)
            heappush(unused, top)
        else:
            heappush(unused, val)

    for v in g[0]:
        heappush(unused, v)

    q_init = max(0, k - min_x)
    for v in g[1][q_init:]:
        heappush(unused, v)
    for v in g[2][q_init:]:
        heappush(unused, v)

    cur_q = q_init
    inf = 10 ** 18
    ans = inf

    for x in range(min_x, max_x + 1):
        q = max(0, k - x)
        while cur_q > q:
            cur_q -= 1
            if cur_q < len(g[1]):
                add_pool(g[1][cur_q])
            if cur_q < len(g[2]):
                add_pool(g[2][cur_q])
        rem = m - x - 2 * q
        if rem < 0:
            continue
        while len(used) < rem and unused:
            v = heappop(unused)
            sum_used += v
            heappush(used, -v)
        while len(used) > rem:
            v = -heappop(used)
            sum_used -= v
            heappush(unused, v)
        if len(used) == rem:
            total = pref[3][x] + pref[1][q] + pref[2][q] + sum_used
            if total < ans:
                ans = total

    sys.stdout.write(str(ans if ans < inf else -1) + '\n')

if __name__ == '__main__':
    solve()