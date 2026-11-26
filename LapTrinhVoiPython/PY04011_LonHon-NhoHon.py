import sys
from collections import deque

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    ptr = 1
    name_to_id = {}
    edges = []
    for _ in range(n):
        u_name = raw[ptr]
        op = raw[ptr + 1]
        v_name = raw[ptr + 2]
        ptr += 3
        if u_name not in name_to_id:
            name_to_id[u_name] = len(name_to_id)
        if v_name not in name_to_id:
            name_to_id[v_name] = len(name_to_id)
        u = name_to_id[u_name]
        v = name_to_id[v_name]
        if op == '>':
            edges.append((u, v))
        else:
            edges.append((v, u))
    num_nodes = len(name_to_id)
    adj = [[] for _ in range(num_nodes)]
    in_degree = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if count == num_nodes:
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    solve()