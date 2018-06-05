# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
#
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
#
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false



def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is not None and q is not None and p.val == q.val and p.left is None and q.left is None and p.right is None and q.right is None:
        return True
    elif p is not None and q is not None and p.val != q.val and p.left is None and q.left is None and p.right is None and q.right is None:
        return False
    if p is None and q is None:
        return True
    if p is not None and q is not None and p.val == q.val and self.isSameTree(p.left,q.left) == True and self.isSameTree(p.right, q.right) == True:
        return True
    return False