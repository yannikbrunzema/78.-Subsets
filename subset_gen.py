def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]  # add empty set to result

    def backtrack(index, current):
        if index >= len(nums):
            return
        else:
            current.append(nums[index])
            res.append(current.copy())
            backtrack(index + 1, current)  # include nums[index]
            current.pop()
            backtrack(index + 1, current)  # don't include nums[index]

    backtrack(0, [])

    return res


