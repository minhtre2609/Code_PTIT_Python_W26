import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    n = int(d[0])
    out = []
    def backtrack(s, has2, has3, has5, has7, L):
        if len(s) == L:
            if has2 and has3 and has5 and has7 and s[-1] != '2':
                out.append(s)
            return
        backtrack(s + '2', True, has3, has5, has7, L)
        backtrack(s + '3', has2, True, has5, has7, L)
        backtrack(s + '5', has2, has3, True, has7, L)
        backtrack(s + '7', has2, has3, has5, True, L)

    for L in range(4, n + 1):
        backtrack('', False, False, False, False, L)

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()