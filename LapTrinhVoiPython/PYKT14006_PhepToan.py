import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    A = [int(x) for x in data[2:2 + n]]
    strs = [f"({x})" if x < 0 else str(x) for x in A]
    out = []

    def dfs(idx, cur_sum, last_term, expr):
        if idx == n:
            if cur_sum + last_term == m:
                out.append(f"{expr}={m}")
            return
        v = A[idx]
        s = strs[idx]
        dfs(idx + 1, cur_sum + last_term, v, expr + "+" + s)
        dfs(idx + 1, cur_sum + last_term, -v, expr + "-" + s)
        dfs(idx + 1, cur_sum, last_term * v, expr + "*" + s)

    dfs(1, 0, A[0], strs[0])
    if not out:
        sys.stdout.write("IMPOSSIBLE\n")
    else:
        sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()