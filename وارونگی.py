def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_merge = merge(left, right)
        return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    i = j = inv_count = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, inv_count

N = int(input())
A = [int(input()) for _ in range(N)]
_, counter = merge_sort(A)
d = counter % 100000
print(d)
