n = int(input())
counts = {}
topic = ""
for _ in range(n):
    line = input().strip()
    if not line:
        topic = ""
    elif not topic:
        topic = line
        if topic not in counts:
            counts[topic] = 0
    else:
        counts[topic] += 1

for k, v in counts.items():
    print(f"{k}: {v}")