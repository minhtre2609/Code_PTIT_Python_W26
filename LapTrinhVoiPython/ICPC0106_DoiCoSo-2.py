import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    num_tests = int(next(iterator))
    hex_chars = "0123456789ABCDEF"
    k_map = {2: 1, 4: 2, 8: 3, 16: 4}
    
    out = []
    for _ in range(num_tests):
        b = int(next(iterator))
        s = next(iterator)
        k = k_map[b]
        rem = len(s) % k
        if rem != 0:
            s = "0" * (k - rem) + s
        res = []
        for i in range(0, len(s), k):
            chunk = s[i:i+k]
            res.append(hex_chars[int(chunk, 2)])
        out.append("".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
