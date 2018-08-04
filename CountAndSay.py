# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
#
# Example 2:
#
# Input: 4
# Output: "1211"



# def countAndSay(n):
#     """
#     :type n: int
#     :rtype: str
#     """
#     dict = {}
#     dict[1] = '1'
#     dict[2] = '11'
#     for i in range(3, n+1):
#         previousStr = dict[i - 1]
#         generatedStr = ""
#         match = 1
#         for j in range(1, len(previousStr)):
#             if previousStr[j] == previousStr[j - 1]:
#                 match = match + 1
#                 if j == len(previousStr) - 1:
#                     generatedStr = generatedStr + str(match) + str(previousStr[j - 1])
#             else:
#                 generatedStr = generatedStr + str(match) + str(previousStr[j - 1])
#                 match = 1
#                 if j == len(previousStr) - 1:
#                     generatedStr = generatedStr + str(1) + str(previousStr[j])
#         dict[i] = generatedStr
#     return dict[n]
#
# print(countAndSay(6))


def numMagicSquaresInside( grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count = 0
    for j in range(len(grid) - 2):
        for i in range(len(grid[0]) - 2):
            X_i_j = [row[0 + i:3 + i] for row in grid[0 + j:3 + j]]

            if (X_i_j[0][0] + X_i_j[1][0] + X_i_j[2][0] == X_i_j[0][1] + X_i_j[1][1] + X_i_j[2][1] == X_i_j[0][2] + X_i_j[1][2] + X_i_j[2][2]) and (X_i_j[0][0] + X_i_j[0][1] + X_i_j[0][2] == X_i_j[1][0] + X_i_j[1][1] + X_i_j[1][2] == X_i_j[2][0] + X_i_j[2][1] + X_i_j[2][2]) and (X_i_j[0][0] + X_i_j[1][1] + X_i_j[2][2] == X_i_j[0][2] + X_i_j[1][1] + X_i_j[2][0] == X_i_j[0][1] + X_i_j[1][1] + X_i_j[2][1]):
                count = count+1
    return count

print(numMagicSquaresInside([[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]))