# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertListNode(self, dummyHead, node):
        """
        insert node to the list starting at dummyHead.next
        return node
        """
        assert node.next is None

        insertBefore = dummyHead

        while insertBefore.next and insertBefore.next.val < node.val:
            insertBefore = insertBefore.next

        node.next = insertBefore.next
        insertBefore.next = node

        return node

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(float('-inf'))
        lastNode = None
        tail = dummyHead

        while head:
            node = head
            head = head.next
            node.next = None

            if tail and tail.val <= node.val:
                self.insertListNode( tail, node )
                tail = node
            elif lastNode and lastNode.val <= node.val:
                self.insertListNode( lastNode, node )
            else:
                self.insertListNode( dummyHead, node )

            lastNode = node

        return dummyHead.next