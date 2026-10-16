n = int(input())
diem = []

for i in range(n):
    diem.append(int(input()))

diem.sort()
nho_nhat = diem[0]

while nho_nhat in diem:
    diem.remove(nho_nhat)

dem = 0
for x in diem:
    if x >= 8:
        dem += 1

print(*diem)
print(dem)