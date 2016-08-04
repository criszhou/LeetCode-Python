# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummyHead1 = ListNode(None)
        dummyHead2 = ListNode(None)
        thisTail = dummyHead1
        nextTail = dummyHead2

        node = head
        thisTailIsOdd = True

        while node:

            newNode = node.next
            thisTail.next = node
            thisTail = node
            thisTail.next = None

            thisTail, nextTail = nextTail, thisTail
            thisTailIsOdd = not thisTailIsOdd

            node = newNode

        if thisTailIsOdd:
            thisTail.next = dummyHead2.next
        else:
            nextTail.next = dummyHead2.next

        return dummyHead1.next