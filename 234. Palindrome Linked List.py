# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None

        while head:
            nextHead = head.next
            head.next = newHead
            newHead = head
            head = nextHead

        return newHead

    def sameList(self, head1, head2):
        while head1 and head2 and head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        return head1 is None and head2 is None

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # determine listLength first
        listLength = 0
        node = head
        while node:
            node = node.next
            listLength += 1

        # break list to first half, mid, second half
        node = head
        for i in range(listLength // 2 - 1):
            node = node.next
        beforeMid = node

        # split into 2 or 3 pieces, first half, second half, and maybe mid node
        if listLength % 2 == 0:
            head1 = head
            head2 = beforeMid.next
            beforeMid.next = None
        else:
            head1 = head
            mid = beforeMid.next
            beforeMid.next = None
            head2 = mid.next
            mid.next = None

        # reverse second half, and compare first half and second half
        head2 = self.reverseList(head2)
        ret = self.sameList(head1, head2)

        # change things back
        head2 = self.reverseList(head2)
        if listLength % 2 == 0:
            beforeMid.next = head2
        else:
            beforeMid.next = mid
            mid.next = head2

        return ret