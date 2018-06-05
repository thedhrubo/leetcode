# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#     a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
# Return false.

def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def totalDepth(root, level=0):
        if not root:
            return level;
        leftLevel = totalDepth(root.left, level + 1)
        rightLevel = totalDepth(root.right, level + 1)
        if abs(leftLevel - rightLevel) > 1:
            return -1
        else:
            return max(leftLevel, rightLevel)

    if not root:
        return True
    else:
        if totalDepth(root) > 0:
            return True
        else:
            return False
