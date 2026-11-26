with open("SOTAY.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

contacts = []
date = ""
i = 0
while i < len(lines):
    if lines[i].startswith("Ngay "):
        date = lines[i][5:].strip()
        i += 1
    else:
        name = lines[i]
        phone = lines[i + 1]
        contacts.append((name, phone, date))
        i += 2

contacts.sort(key=lambda item: (item[0].split()[-1], " ".join(item[0].split()[:-1])))

with open("DIENTHOAI.txt", "w", encoding="utf-8") as f:
    for name, phone, d in contacts:
        f.write(f"{name}: {phone} {d}\n")