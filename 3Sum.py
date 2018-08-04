def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    list = []
    i = 0
    while sum(nums[i:i + 3]) <= 0 or i + 2 <= len(nums):
        if sum(nums[i:i + 3]) == 0:
            list.append(nums[i:i + 3])
        i = i + 1
    return list

print(threeSum([-1, 0, 1, 2, -1, -4]))