# Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.
#
# Examples:
#
# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2
#
# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies arr[i] == i.
#
# Constraints:
#
#     [time limit] 5000ms
#
#     [input] array.integer arr
#         1 ≤ arr.length ≤ 100
#
#     [output] integer


def index_equals_value_search(arr):
    pass  # your code goes here

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (end + start) // 2
        if arr[mid] - mid < 0:
            start = mid + 1
        elif arr[mid] - mid > 0:
            end = mid - 1
        else:
            return mid
    return -1


print(index_equals_value_search([-8,1,2,5]))