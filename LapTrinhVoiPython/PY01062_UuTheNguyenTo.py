import sys

p_dig = {'2', '3', '5', '7'}

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    for k in range(1, t + 1):
        s = d[k]
        n = len(s)
        cp = sum(1 for c in s if c in p_dig)
        if is_prime(n) and cp > n - cp:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()