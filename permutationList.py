# def permutList(l):
#     if not l:
#             return [[]]
#     res = []
#     for e in l:
#             temp = l[:]
#             temp.remove(e)
#             res.extend([[e] + r for r in permutList(temp)])
#
#     return res
#
# print(permutList([1, 2, 3]))

def permute( nums):
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
        res.extend([i]+ x for x in permute(temp))
    return res


def permuteRecursion( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    for i in nums:

        return res

print(permute([1, 2, 3]))




