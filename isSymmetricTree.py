# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3


def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root:
        return self.helper(root.left, root.right)
    return True


def helper(self, leftNode, rightNode):
    if leftNode is None and rightNode is None:
        return True
    elif leftNode is None or rightNode is None:
        return False
    elif leftNode and rightNode:
        if leftNode.val != rightNode.val:
            return False
    return self.helper(leftNode.left, rightNode.right) and self.helper(leftNode.right, rightNode.left)