import math

#len cua list la do dai danh sach
#truy cap thislist[1], co the su dung chi so am -1 (chi ve phan tu cuoi cung)
# if "apple" in thislist: kiem tra apple co trong thislist khong
#insert(index, value): chen phan tu
#append: noi phan tu vao cuoi list (+=)
#extend: mo rong danh sach
#enumerate(zip(x, y)): enumerate de tao ra index, zip de duyet 2 hoac nhieu danh sach

"""
n = int(input())
tong = n * 8000
if n >= 10:
    tong *= 0.97
giam1 = min(tong * 0.08, 30000)
tien1 = tong - giam1
tien2 = tong
if tong >= 100000:
    tien2 = tong - 20000
print(int(min(tien1, tien2)))

t = int(input())
gio = (t + 59) // 60
if gio <= 2:
    tien = gio * 5000
elif gio <= 5:
    tien = 2 * 5000 + (gio - 2) * 3000
else:
    tien = 2 * 5000 + 3 * 3000 + (gio - 5) * 2000
if t > 480:
    tien += 10000
print(tien)

#So chinh phuong
import math
n = int(input())
k = int(math.sqrt(n))
if k * k == n:
    print("YES")
else:
    print("NO")"""

#tong chan le
n = int(input())
tong = 0.0
for i in range(1, n + 1):
    if i % 2 == 0:
        tong += i
    else:
        tong += 1 / i
print(f"{tong:.6f}")

