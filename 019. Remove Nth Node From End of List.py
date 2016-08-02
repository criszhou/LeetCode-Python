# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        dummyHead.next = head

        fast = head
        for i in range(n - 1):
            fast = fast.next

        slow = dummyHead
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummyHead.next