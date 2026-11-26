import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    num_tests = int(next(iterator))
    for _ in range(num_tests):
        n = int(next(iterator))
        m = int(next(iterator))
        u = int(next(iterator))
        v = int(next(iterator))
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x = int(next(iterator))
            y = int(next(iterator))
            adj[x].append(y)
        
        count = 0
        for node in range(1, n + 1):
            if node == u or node == v:
                continue
            # BFS from u to v without using `node`
            visited = [False] * (n + 1)
            visited[u] = True
            q = deque([u])
            reached = False
            while q:
                curr = q.popleft()
                if curr == v:
                    reached = True
                    break
                for nxt in adj[curr]:
                    if nxt != node and not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            if not reached:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()
