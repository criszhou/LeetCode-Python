# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastNoneNine = None

        node = head
        while node:
            if node.val != 9:
                lastNoneNine = node
            node = node.next

        if not lastNoneNine:
            newHead = ListNode(0)
            newHead.next = head
            head = newHead
            lastNoneNine = head

        lastNoneNine.val += 1
        node = lastNoneNine.next
        while node:
            node.val = 0
            node = node.next

        return head