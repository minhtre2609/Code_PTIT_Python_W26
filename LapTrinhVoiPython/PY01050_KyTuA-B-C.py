import sys

def solve():
    s_in = sys.stdin.read().split()
    if not s_in:
        return
    n = int(s_in[0])
    out = []
    def backtrack(s, ca, cb, cc, L):
        if len(s) == L:
            if ca > 0 and cb >= ca and cc >= cb:
                out.append(s)
            return
        backtrack(s + 'A', ca + 1, cb, cc, L)
        backtrack(s + 'B', ca, cb + 1, cc, L)
        backtrack(s + 'C', ca, cb, cc + 1, L)

    for L in range(3, n + 1):
        backtrack('', 0, 0, 0, L)
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()