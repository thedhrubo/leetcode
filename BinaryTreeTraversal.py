# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
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
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]



def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    List = []
    if root:
        self.totalDepth(root, List, 0)
    List.reverse()
    return List

def totalDepth(self, root, List, depthLevel):
    if root:
        if len(List) > depthLevel and List[depthLevel]:
            List[depthLevel].append(root.val)
        else:
            List.insert(depthLevel, [root.val])

        self.totalDepth(root.left, List, depthLevel + 1)
        self.totalDepth(root.right, List, depthLevel + 1)