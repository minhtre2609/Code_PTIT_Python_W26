import sys

def check(a, op, b, ans):
    if op == '+':
        return a + b == ans
    if op == '-':
        return a - b == ans
    if op == '*':
        return a * b == ans
    if op == '/':
        return b != 0 and a % b == 0 and a // b == ans
    return False

def genn(a):
    ans = []
    if a[0] == '?':
        for i in range(1, 10):
            ans.append(str(i) + a[1:])
    else:
        ans.append(a)
    r = []
    if a[1] == '?':
        for i in ans:
            for j in range(0, 10):
                r.append(i[0] + str(j))
    else:
        r = ans
    return r

def geno(x):
    if x == '?':
        return ['+', '-', '*', '/']
    return [x]

def solve_one(s):
    arr = s.split()
    if len(arr) < 5:
        return 'WRONG PROBLEM!'
    a = genn(arr[0])
    op = geno(arr[1])
    b = genn(arr[2])
    ans = genn(arr[4])
    for i in a:
        for j in op:
            for k in b:
                for m in ans:
                    if check(int(i), j, int(k), int(m)):
                        return f'{i} {j} {k} = {m}'
    return 'WRONG PROBLEM!'

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    for idx in range(1, t + 1):
        if idx < len(lines):
            line = lines[idx].strip()
            if line:
                print(solve_one(line))

if __name__ == '__main__':
    solve()