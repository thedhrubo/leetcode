# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]





def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    returnList = []
    prev = float("inf")
    nums.sort()
    for i in range(0, len(nums)):
        if prev != nums[i]:
            prev = nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum == 0:
                    returnList.append([nums[i], nums[start], nums[end]])
                    start = start + 1
                    end = end - 1
                    while start < end and nums[start] == nums[start - 1]:
                        start = start + 1

                    while start < end and nums[end] == nums[end + 1]:
                        end = end - 1
                elif sum < 0:
                    start = start + 1
                else:
                    end = end - 1
    return returnList


# Another Solution which is taking less time :

    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     returnList = []
    #     posList = []
    #     negList = []
    #     numDict = {}
    #     if len(nums) < 3:
    #         return returnList
    #     for i in nums:
    #
    #         if i in numDict:
    #             numDict[i] += 1
    #         else:
    #             numDict[i] = 1
    #     if 0 in numDict and numDict[0] >= 3:
    #         returnList.append([0, 0, 0])
    #
    #     notDuplicate = set(nums)
    #     for i in notDuplicate:
    #         if i < 0:
    #             negList.append(i)
    #         else:
    #             posList.append(i)
    #     for i in posList:
    #         for j in negList:
    #             if -(i + j) in numDict:
    #                 if (-(i + j) == i and numDict[i] >= 2) or (-(i + j) == j and numDict[j] >= 2) or (
    #                         -(i + j) > j and -(i + j) < i):
    #                     returnList.append([i, j, -(i + j)])
    #
    #     return returnList

print(threeSum([-1,0,1,2,-1,-4]))