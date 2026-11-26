n, m, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

vis = [False] * (n + 1)
q = [x]
vis[x] = True
while q:
    u = q.pop()
    for v in adj[u]:
        if not vis[v]:
            vis[v] = True
            q.append(v)

res = []
for i in range(1, n + 1):
    if not vis[i]:
        res.append(i)

if not res:
    print(0)
else:
    for v in res:
        print(v)