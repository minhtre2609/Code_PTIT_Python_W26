import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    num_tests = int(next(iterator))
    for _ in range(num_tests):
        n = int(next(iterator))
        arr = [int(next(iterator)) for _ in range(n)]
        total = 0
        for i in range(n - 1):
            mn = min(arr[i], arr[i + 1])
            mx = max(arr[i], arr[i + 1])
            while mn * 2 < mx:
                total += 1
                mn *= 2
        print(total)

if __name__ == '__main__':
    solve()
