# Move Zeroes # Facebook interview problems
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count = 0
    while 0 in nums:
        count = count+1
        nums.remove(0)
    zeroList = [0] * count
    nums.extend(zeroList)
    return nums
print(moveZeroes([0,1,0,3,12]))