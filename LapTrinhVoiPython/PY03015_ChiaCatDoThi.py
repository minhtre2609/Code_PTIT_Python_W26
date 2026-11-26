import sys

def count_components(n, adj, removed):
    visited = [False] * (n + 1)
    visited[removed] = True
    comp = 0
    for i in range(1, n + 1):
        if not visited[i]:
            comp += 1
            queue = [i]
            visited[i] = True
            for u in queue:
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
    return comp

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    ptr = 0
    t = int(raw[ptr])
    ptr += 1
    out = []
    for _ in range(t):
        n = int(raw[ptr])
        m = int(raw[ptr + 1])
        ptr += 2
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(raw[ptr])
            v = int(raw[ptr + 1])
            adj[u].append(v)
            adj[v].append(u)
            ptr += 2
        max_comp = 1
        best_u = 0
        for u in range(1, n + 1):
            c = count_components(n, adj, u)
            if c > max_comp:
                max_comp = c
                best_u = u
        out.append(str(best_u))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()