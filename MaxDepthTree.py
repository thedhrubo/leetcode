# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.



def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
        nodes = self.totalDepth(root)
        return nodes
    else:
        return 0


def totalDepth(self, root):
    if root.left or root.right:
        if root.left and root.right:
            return 1 + max(self.totalDepth(root.left), self.totalDepth(root.right))
        elif root.left and root.right is None:
            return 1 + self.totalDepth(root.left)
        elif root.right and root.left is None:
            return 1 + self.totalDepth(root.right)
    else:
        return 1