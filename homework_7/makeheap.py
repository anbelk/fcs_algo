def sift_up(arr: list, idx: int) -> list:
    curr_idx = idx

    while curr_idx:
        next_idx = (curr_idx - 1) // 2
        if arr[next_idx] > arr[curr_idx]:
            arr[next_idx], arr[curr_idx] = arr[curr_idx], arr[next_idx]
        curr_idx = next_idx
    
    return arr


def makeheap_n_log_n(arr: list) -> list:
    heap = []

    for i in range(len(arr)):
        heap.append(arr[i])
        sift_up(heap, i)
    
    return heap


def sift_down(arr: list, idx: int) -> list:
    curr_idx = idx

    while True:
        left_child_idx, right_child_idx = 2 * curr_idx + 1, 2 * curr_idx + 2

        if left_child_idx >= len(arr):
            break

        if right_child_idx >= len(arr):
            if arr[left_child_idx] < arr[curr_idx]:
                arr[left_child_idx], arr[curr_idx] = arr[curr_idx], arr[left_child_idx]
            break

        left_child, right_child = arr[left_child_idx], arr[right_child_idx]

        next_idx = left_child_idx if left_child < right_child else right_child_idx

        if arr[next_idx] < arr[curr_idx]:
            arr[next_idx], arr[curr_idx] = arr[curr_idx], arr[next_idx]
            curr_idx = next_idx
        else:
            break

    return arr


def makeheap(arr: list) -> list:
    for i in range(len(arr), -1, -1):
        sift_down(arr, i)
    
    return arr