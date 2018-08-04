# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    temp = [0] * len(nums)
    temp1 = [0] * len(nums)
    temp[0] = 1
    temp1[len(nums) - 1] = 1
    mult = 1
    for i in range(1, len(nums)):
        temp[i] = mult
        mult = mult * nums[i]
    mult = 1 * nums[len(nums)-1]

    for i in range(len(nums) - 1, -1, -1):
        temp1[i] = mult
        mult = mult * nums[i]
    for i in range(0, len(temp) - 1):
        temp[i] = temp[i] * temp1[i]

    return temp;

print(productExceptSelf([0,0]))