from tracer import tracer

@tracer
def _backtrack_permutations(idx, permutation, nums, n, result):
    if idx == n:
        result.append(list(permutation))
        return
    for i in range(n):
        if nums[i] in permutation:
            continue
        permutation.append(nums[i])
        _backtrack_permutations(idx + 1, permutation, nums, n, result)
        permutation.pop()

def permutations(nums):
    result = []
    n = len(nums)
    if n == 0:
        return [[]]
    _backtrack_permutations(0, [], nums, n, result)
    return result