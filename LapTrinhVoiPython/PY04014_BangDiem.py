import sys
from decimal import Decimal, ROUND_HALF_UP

def get_rank(avg):
    if avg >= Decimal('9.0'):
        return "XUAT SAC"
    if avg >= Decimal('8.0'):
        return "GIOI"
    if avg >= Decimal('7.0'):
        return "KHA"
    if avg >= Decimal('5.0'):
        return "TB"
    return "YEU"

def solve():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return
    n = int(lines[0])
    students = []
    idx = 1
    for i in range(1, n + 1):
        name = lines[idx]
        scores = [Decimal(x) for x in lines[idx + 1].split()]
        idx += 2
        s = sum(scores) + scores[0] + scores[1]
        avg = (s / Decimal(12)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_id = f"HS{i:02d}"
        rank = get_rank(avg)
        students.append((s_id, name, avg, rank))
    students.sort(key=lambda x: (-x[2], x[0]))
    for s_id, name, avg, rank in students:
        print(f"{s_id} {name} {avg} {rank}")

if __name__ == '__main__':
    solve()