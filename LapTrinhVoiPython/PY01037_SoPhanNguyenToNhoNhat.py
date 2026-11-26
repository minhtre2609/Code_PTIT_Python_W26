import sys
import bisect

a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800, 14414400, 17297280, 21621600]
a_str = [str(x) + '\n' for x in a]

def solve():
    f = sys.stdin
    first_line = f.readline()
    if not first_line:
        return
    t = int(first_line.strip())
    bisect_left = bisect.bisect_left
    out = []
    app = out.append
    write = sys.stdout.write
    for line in f:
        s = line.strip()
        if not s:
            continue
        app(a_str[bisect_left(a, int(s))])
        if len(out) >= 10000:
            write(''.join(out))
            out.clear()
    if out:
        write(''.join(out))

if __name__ == '__main__':
    solve()