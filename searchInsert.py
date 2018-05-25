# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
#
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
#
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
#
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0




def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(0, len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

print(searchInsert([1,3,5,6], 5))