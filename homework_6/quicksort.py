import random

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort_iterative(array):
    array = array.copy()
    stack = [(0, len(array) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        p = partition(array, low, high)
        stack.append((low, p - 1))
        stack.append((p + 1, high))
    return array

def quicksort_rec(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort_rec(left) + equal + quicksort_rec(right)

def quickselect(array, k):
    k_idx = len(array) - k
    low, high = 0, len(array) - 1
    while low <= high:
        pivot_index = random.randint(low, high)
        array[pivot_index], array[high] = array[high], array[pivot_index]
        p = partition(array, low, high)
        if p == k_idx:
            return array[p]
        elif p < k_idx:
            low = p + 1
        else:
            high = p - 1