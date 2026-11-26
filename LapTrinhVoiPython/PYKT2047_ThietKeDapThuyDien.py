import sys
from bisect import bisect_left

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        L = [int(x) for x in data[idx:idx + n]]
        idx += n
        H = [int(x) for x in data[idx:idx + n]]
        idx += n
        prefH = [0] * (n + 1)
        s = 0
        for i in range(n):
            s += H[i]
            prefH[i + 1] = s
        st = []
        cap = [0] * n
        for i in range(n):
            hi = H[i]
            while st and H[st[-1]] <= hi:
                st.pop()
            if not st:
                cap[i] = L[i] * hi - prefH[i]
            else:
                j = st[-1]
                cap[i] = cap[j] + (L[i] - L[j] - 1) * hi - (prefH[i] - prefH[j + 1])
            st.append(i)
        q = int(data[idx])
        idx += 1
        for _ in range(q):
            k = int(data[idx])
            idx += 1
            out.append(str(bisect_left(cap, k)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()