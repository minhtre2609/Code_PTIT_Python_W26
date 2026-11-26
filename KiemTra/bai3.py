t = int(input())
for _ in range(t):
    n, m, u, v = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
    ans = 0
    for skip in range(1, n + 1):
        if skip == u or skip == v:
            continue
        visited = [False] * (n + 1)
        visited[u] = True
        visited[skip] = True
        q = [u]
        while q:
            curr = q.pop(0)
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        if not visited[v]:
            ans += 1
    print(ans)
