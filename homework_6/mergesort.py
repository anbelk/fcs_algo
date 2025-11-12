def merge(left, right):
    i = j = 0
    merged = []
    while True:
        if i == len(left):
            merged += right[j:]
            break
        if j == len(right):
            merged += left[i:]
            break
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged

def mergesort_iterative(array):
    array = array.copy()
    N = len(array)
    size = 1
    while size < N:
        merged = []
        for i in range(0, N, 2 * size):
            left = array[i:i + size]
            right = array[i + size:i + 2 * size]
            merged += merge(left, right)
        array = merged
        size *= 2
    return array

def mergesort_rec(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergesort_rec(array[:mid])
    right = mergesort_rec(array[mid:])
    return merge(left, right)