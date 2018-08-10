#  On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
#
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
#
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
#
# Note:
#
#     cost will have a length in the range [2, 1000].
#     Every cost[i] will be an integer in the range [0, 999].

# We can solve this problem in the naive ways through the recursive way :
# In that case time complexity will be: O(2^n)
# space complexity will be : O(n)
#
# The code is :


# def minCostClimbingStairs(cost):
#     """
#     :type cost: List[int]
#     :rtype: int
#     """
#     return min(calRecursion(len(cost)-1, cost), calRecursion(len(cost)-2, cost))
#
#
# def calRecursion(index, cost):
#     if index == 1:
#         return cost[1]
#     if index == 0:
#         return cost[0]
#     return cost[index] + min(calRecursion(index - 2, cost), calRecursion(index - 1, cost))


# Now we can improve the recursion through the memoization. Then we can solve the problem in O(n) time complexity.
#
# The code is:

# def minCostClimbingStairs(cost):
#     """
#     :type cost: List[int]
#     :rtype: int
#     """
#     dict = {}
#     return min(calRecursion(len(cost) - 1, cost, dict), calRecursion(len(cost) - 2, cost, dict))
#
#
# def calRecursion(index, cost, dict):
#     if index == 1:
#         return cost[1]
#     if index == 0:
#         return cost[0]
#     if index in dict:
#         return dict[index]
#     else:
#         dict[index] = cost[index] + min(calRecursion(index - 2, cost, dict),
#                                         calRecursion(index - 1, cost, dict))
#         return dict[index]


# But still we can improve our code by optimizing the space complexity to O(1)
#
# The code will be:

def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    a = b = 0
    for i in range(0, len(cost)):
        a, b = cost[i] + min(a, b), a
    return min(a, b)

print(minCostClimbingStairs([0, 0, 0, 1]))