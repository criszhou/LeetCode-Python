# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        dummyHead.next = head

        node = dummyHead

        while node.next and node.next.next:
            next1 = node.next
            next2 = node.next.next
            next3 = node.next.next.next # may be None

            node.next = next2
            next2.next = next1
            next1.next = next3

            node = next1

        return dummyHead.next