# 112. Path Sum

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    if self.calculateSum(root, sum, 0):
        return True
    else:
        return False


def calculateSum(self, root, sum, calculateSum):
    if root:
        if not root.left and not root.right and sum == calculateSum + root.val:
            return True
        return self.calculateSum(root.left, sum, calculateSum + root.val) or self.calculateSum(root.right, sum,
                                                                                               calculateSum + root.val)
