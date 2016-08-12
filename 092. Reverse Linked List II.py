# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head

        dummyHead = ListNode(None)
        dummyHead.next = head

        prevNode = None
        node = dummyHead

        for i in range(m):
            prevNode = node
            node = node.next

        # now node is the first one in reversed part, will be the last one
        beforeRev = prevNode # the node before the reversed part
        nextNode = node.next # the next one to handle, to be inserted after beforeRev
        node.next = None

        for i in range(n-m):
            # insert new nodes between beforeRev and beforeRev.next
            newNextNode = nextNode.next
            nextNode.next = beforeRev.next
            beforeRev.next = nextNode
            nextNode = newNextNode

        # concatenate last one in reversed part with list after reversed part
        node.next = nextNode

        return dummyHead.next