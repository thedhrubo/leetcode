def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    i = j = 0
    list = []
    while i < len(nums1) and j < len(nums2):
        if (nums1[i] == nums2[j]):
            list.append(nums1[i])
            i = i + 1
            j = j + 1
        elif nums1[i] > nums2[j]:
            j = j + 1
        else:
            i = i + 1
    return list


def find_duplicates(arr1, arr2):
    dict = {}
    list = []

    for i in arr1:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    for j in arr2:
        if j in dict:
            list.append(j)
            dict[j] = dict[j] - 1
    return list

# print(intersect([1,1], [1]))

print(find_duplicates([2, 2], [2,2]))