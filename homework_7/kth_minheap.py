import heapq
from makeheap import makeheap, sift_down


def kth_minheap(nums, k):
    heap = nums[:k]

    makeheap(heap)

    for x in nums[k:]:
        if x > heap[0]:
            heap[0] = x
            sift_down(heap, 0)

    return heap[0]


def kth_minheap_hq(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for x in nums[k:]:
        if x > heap[0]:
            heapq.heappushpop(heap, x)
    
    return heap[0]
