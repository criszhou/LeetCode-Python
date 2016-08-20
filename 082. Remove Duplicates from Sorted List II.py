# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        dummyHead.next = head
        node = dummyHead

        while node and node.next and node.next.next:
            if node.next.val != node.next.next.val:
                node = node.next
            else:
                val = node.next.val
                while node.next and node.next.val == val:
                    node.next = node.next.next

        return dummyHead.next