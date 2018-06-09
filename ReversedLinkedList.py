# Facebook problem : Reverse Linked List

# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# Iterative one

def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


# Now the recursice one

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.recursive(head, None)

    def recursive(self, head, prev):
        if head:
            curr = head
            head = head.next
            curr.next = prev
            return self.recursive(head, curr)
        else:
            return prev