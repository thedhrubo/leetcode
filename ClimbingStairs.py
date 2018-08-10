# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step



def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # the complexity of the commented code is 2^n but we do not need any storage. But leetcode expects more efficient runtime algorithm which is
    # the uncommented code.

    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 1
    # return climbStairs(n - 1) + climbStairs(n - 2)

    # linear time efficient code.

    # Complexity Analysis :
    # single loop till n so time complexity O(n)
    # and the space complexity is also O(n) as the list contains the n elements
#     By the way, this way to divide the problems in the sub problems is called dynamic programming.
    fibs = [1, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 2] + fibs[i - 1])
    return fibs[n]

# we can do the same problem with memoization through recursion

# although this is recursion, it will go through the n iterations for which time complexity is O(n)
# space complexity is also O(n)

    # def climbStairs(n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dict = {}
    #     return climbRecursion(n, 0, dict)
    #
    # def climbRecursion(n, count, dict):
    #     if n == 0:
    #         return count + 1
    #     if n < 0:
    #         return False
    #     if n in dict:
    #         return dict[n]
    #     else:
    #         dict[n] = climbRecursion(n - 1, count, dict) + climbRecursion(n - 2, count, dict)
    #         return dict[n]

# To minimize the space complexity we can following the following way:

    # def climbStairs(n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     a = b = 1
    #     for i in range(n):
    #         a, b = b, a + b
    #     return a

print(climbStairs(35))