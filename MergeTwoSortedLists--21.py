# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# We can solve it in iterative or recursive way :
#
# Iterative way :

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val > l2.val:
             curr.next = l2
             l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next