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