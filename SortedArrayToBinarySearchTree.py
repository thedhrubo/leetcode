# 108. Convert Sorted Array to Binary Search Tree
#
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return None

    headNode = len(nums) // 2
    root = TreeNode(nums[headNode])
    root.left = self.sortedArrayToBST(nums[:headNode])
    root.right = self.sortedArrayToBST(nums[headNode + 1:])
    return root