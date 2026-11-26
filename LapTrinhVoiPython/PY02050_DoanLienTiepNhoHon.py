import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    ptr = 0
    t = int(raw[ptr])
    ptr += 1
    out = []
    for _ in range(t):
        n = int(raw[ptr])
        ptr += 1
        arr = [int(x) for x in raw[ptr:ptr + n]]
        ptr += n
        res = [0] * n
        stack = []
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] <= val:
                stack.pop()
            res[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        out.append(" ".join(map(str, res)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()