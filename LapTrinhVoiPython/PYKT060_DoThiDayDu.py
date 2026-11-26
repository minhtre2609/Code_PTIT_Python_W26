n = int(input())
m = int(input())
adj = [set() for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

vis = [False] * (n + 1)
ok = True
for i in range(1, n + 1):
    if not vis[i]:
        comp = []
        q = [i]
        vis[i] = True
        while q:
            u = q.pop()
            comp.append(u)
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
        k = len(comp)
        for u in comp:
            if len(adj[u]) != k - 1:
                ok = False
                break
    if not ok:
        break

if ok:
    print("YES")
else:
    print("NO")