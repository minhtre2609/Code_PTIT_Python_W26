import sys

def solve():
    lines = sys.stdin
    first = lines.readline()
    while first and not first.strip():
        first = lines.readline()
    if not first:
        return
    n = int(first.strip())
    ans = 0
    stack = []
    for _ in range(n):
        line = lines.readline()
        while line and not line.strip():
            line = lines.readline()
        if not line:
            break
        x = int(line.strip())
        cnt = 1
        while stack and stack[-1][0] <= x:
            top_val, top_cnt = stack[-1]
            ans += top_cnt
            if top_val == x:
                cnt += top_cnt
            stack.pop()
        if stack:
            ans += 1
        stack.append((x, cnt))
    print(ans)

if __name__ == '__main__':
    solve()