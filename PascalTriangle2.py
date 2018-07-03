# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    returnList = []

    for i in range(1, rowIndex + 2):
        innerList = []
        for j in range(0, i):
            if j == 0 or j + 1 == i:
                innerList.append(1)
            else:
                innerList.append(returnList[j] + returnList[j - 1])
        returnList = innerList
    return returnList

print(getRow(3))