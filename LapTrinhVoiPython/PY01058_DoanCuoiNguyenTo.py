import sys

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
        val = int(s[-4:])
        if is_prime(val):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()