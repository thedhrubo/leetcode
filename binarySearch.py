import math;
def binarySearch(list, expectedNum):
    if len(list) == 0:
        return False
    if len(list) == 1:
        if list[0] == expectedNum:
            return True
        else:
            return False
    else:
        list1 = list[0:math.floor(len(list)/2)]
        list2 = list[math.floor(len(list)/2):len(list)]
        return binarySearch(list1, expectedNum) or binarySearch(list2, expectedNum)
print(binarySearch([], 10))

