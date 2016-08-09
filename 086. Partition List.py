# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummyHead1 = ListNode(None)
        dummyHead2 = ListNode(None)
        tail1 = dummyHead1
        tail2 = dummyHead2

        node = head
        while node:
            if node.val < x:
                tail1.next = node
                node = node.next
                tail1 = tail1.next
                tail1.next = None
            else:
                tail2.next = node
                node = node.next
                tail2 = tail2.next
                tail2.next = None

        tail1.next = dummyHead2.next
        return dummyHead1.next