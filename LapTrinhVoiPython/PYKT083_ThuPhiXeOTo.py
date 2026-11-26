price = {
    ("Xe_con", "5"): 10000,
    ("Xe_con", "7"): 15000,
    ("Xe_tai", "2"): 20000,
    ("Xe_khach", "29"): 50000,
    ("Xe_khach", "45"): 70000,
}

n = int(input())
totals = {}
for _ in range(n):
    plate, kind, seats, direction, date = input().split()
    if direction == "IN":
        totals[date] = totals.get(date, 0) + price[(kind, seats)]

for date, amount in totals.items():
    print(f"{date}: {amount}")