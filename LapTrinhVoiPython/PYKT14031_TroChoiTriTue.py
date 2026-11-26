import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    tokens = data[3:]
    if len(tokens) == 1 and len(tokens[0]) == n:
        t_list = [1 if ch == '1' else 0 for ch in tokens[0]]
    else:
        t_list = [int(x) for x in tokens[:n]]

    full_mask = (1 << n) - 1
    t_mask = 0
    for i, v in enumerate(t_list):
        if v:
            t_mask |= (1 << i)

    w_cur = full_mask ^ t_mask
    if m > 1:
        front = []
        back = [(w_cur, w_cur, w_cur)]
        for _ in range(m - 2, -1, -1):
            if not front:
                all_1, any_1 = back[-1][1], back[-1][2]
            elif not back:
                all_1, any_1 = front[-1][1], front[-1][2]
            else:
                all_1 = front[-1][1] & back[-1][1]
                any_1 = front[-1][2] | back[-1][2]

            a_rot = (all_1 >> 1) | ((all_1 & 1) << (n - 1))
            b_rot = (any_1 >> 1) | ((any_1 & 1) << (n - 1))
            w_cur = a_rot | (b_rot & t_mask)

            if not back:
                back.append((w_cur, w_cur, w_cur))
            else:
                _, prev_a, prev_o = back[-1]
                back.append((w_cur, prev_a & w_cur, prev_o | w_cur))

            if len(front) + len(back) > k:
                if not front:
                    while back:
                        x, _, _ = back.pop()
                        if not front:
                            front.append((x, x, x))
                        else:
                            _, fa, fo = front[-1]
                            front.append((x, fa & x, fo | x))
                front.pop()

    res = ['1' if (w_cur >> i) & 1 else '0' for i in range(n)]
    sys.stdout.write(' '.join(res) + '\n')

if __name__ == '__main__':
    solve()