def merge_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

lst = [3, 1, 4, 1, 5, 900, 2, 6, 5, 3, 5, 20, 103, 304, 205, 106, 707, 108, 1090, 110]
print(merge_sort(lst))