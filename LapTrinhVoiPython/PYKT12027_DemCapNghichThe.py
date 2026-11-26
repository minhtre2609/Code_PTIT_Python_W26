import sys

def merge_sort(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, inv_left = merge_sort(a[:mid])
    right, inv_right = merge_sort(a[mid:])
    
    merged = []
    inv_count = inv_left + inv_right
    i = j = 0
    len_left = len(left)
    len_right = len(right)
    
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len_left - i
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    _, ans = merge_sort(a)
    print(ans)