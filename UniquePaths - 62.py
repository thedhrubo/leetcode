# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28

# Recursive solution with memoization :

# def uniquePaths(m, n):
#     """
#     :type m: int
#     :type n: int
#     :rtype: int
#     """
#     a = 1
#     b = 1
#     dict = {}
#     return recursionPath(a, b, m, n, dict)
#
#
# def recursionPath(a, b, m, n, dict):
#     if a > m or b > n:
#         return False
#     if a == m and b == n:
#         return 1
#     if (a, b) in dict:
#         return dict[a, b]
#     dict[a, b] = recursionPath(a + 1, b, m, n, dict) + recursionPath(a, b + 1, m, n, dict)
#     return dict[a, b]

# Iterative solution with dynamice programming:

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dict = {}
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dict[i, j] = 1
            else:
                dict[i, j] = dict[i - 1, j] + dict[i, j - 1]
    return dict[m - 1, n - 1]


# For the recursive we need more space comparing with the iterative one. But the run time complexity will be similar.True

print(uniquePaths(7,3))