# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLenTail(self, node):
        """
        return a pair (length, tail)
        """
        length = 1
        while node.next:
            node = node.next
            length += 1
        return length, node


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        lenA, tailA = self.getLenTail(headA)
        lenB, tailB = self.getLenTail(headB)

        if tailA != tailB:
            return None

        for x in range(lenA-lenB):
            headA = headA.next
        for x in range(lenB-lenA):
            headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
