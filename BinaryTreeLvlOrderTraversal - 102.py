# 102. Binary Tree Level Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    returnList = []
    if root:
        returnList.append([root.val])
        helperRecursion(root.left, returnList, 1) or helperRecursion(root.right, returnList, 1)
    return returnList


def helperRecursion(self, root, returnList, level):
    if root:
        if len(returnList) <= level:
            returnList.append([root.val])
        else:
            returnList[level].append(root.val)
        return helperRecursion(root.left, returnList, level + 1) or helperRecursion(root.right, returnList, level + 1)
    else:
        return None