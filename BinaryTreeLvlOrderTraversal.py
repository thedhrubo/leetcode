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

def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    List = []
    if root:
        self.totalDepth(root, List, 0)
    return List


def totalDepth(self, root, List, depthLevel):
    if root:
        if len(List) > depthLevel and List[depthLevel]:
            List[depthLevel].append(root.val)
        else:
            List.insert(depthLevel, [root.val])

        self.totalDepth(root.left, List, depthLevel + 1)
        self.totalDepth(root.right, List, depthLevel + 1)