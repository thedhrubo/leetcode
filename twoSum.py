def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}

    if len(nums) < 2:
        return False
    for index, val in enumerate(nums):
        if val in dict:
            return [dict[val], index]
        else:
            dict[target - val] = index
    return dict

print(twoSum([3,3], 6))