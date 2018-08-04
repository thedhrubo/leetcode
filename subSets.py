# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]
    res = []
    for i in nums:
        temp = nums[:]
        temp.remove(i)
        for x in subsets(temp):
            x = [i] + x
            res.extend(x)

        # res.extend([] + x for x in subsets(temp))
    return res

print(subsets([1,2,3]))