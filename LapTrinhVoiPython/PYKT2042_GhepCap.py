import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    queries = [int(x) for x in data[1:t + 1]]
    max_n = max(queries) if queries else 0
    if max_n < 1:
        return
    divs = [2] * (max_n + 1)
    divs[0] = 0
    divs[1] = 1
    limit = int(max_n ** 0.5)
    for i in range(2, limit + 1):
        divs[i * i] += 1
        for j in range(i * i + i, max_n + 1, i):
            divs[j] += 2
    sys.stdout.write('\n'.join(str(divs[n]) for n in queries) + '\n')

if __name__ == '__main__':
    solve()