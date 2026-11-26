import sys

parent = list(range(100005))

def find(i):
    path = []
    while parent[i] != i:
        path.append(i)
        i = parent[i]
    for node in path:
        parent[node] = i
    return i

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_i] = root_j

data = sys.stdin.read().split()
if data:
    q = int(data[0])
    idx = 1
    ans = []
    for _ in range(q):
        x = int(data[idx])
        y = int(data[idx + 1])
        z = int(data[idx + 2])
        idx += 3
        
        if z == 1:
            union(x, y)
        else:
            if find(x) == find(y):
                ans.append("1")
            else:
                ans.append("0")
                
    print('\n'.join(ans))