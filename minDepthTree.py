# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
# return its minimum depth = 2.



def minDepth(self, root):
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
            return 1 + min(self.totalDepth(root.left), self.totalDepth(root.right))
        elif root.left and root.right is None:
            return 1 + self.totalDepth(root.left)
        elif root.right and root.left is None:
            return 1 + self.totalDepth(root.right)
    else:
        return 1