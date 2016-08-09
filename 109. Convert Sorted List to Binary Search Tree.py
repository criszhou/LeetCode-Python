# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBSTHelper(self, head, treeSize):
        """
        Moves head forward, and build a balanced tree with the iterated list nodes
        return a pair (treeRoot, newHead)
        """
        if treeSize==0:
            return (None, head)

        if treeSize==1:
            return (TreeNode(head.val), head.next)

        leftTreeSize = treeSize // 2
        rightTreeSize = treeSize - 1 - leftTreeSize

        (leftRoot, rootListNode) = self.sortedListToBSTHelper( head, leftTreeSize )
        root = TreeNode( rootListNode.val )
        rightHead = rootListNode.next
        (rightRoot, currNode) = self.sortedListToBSTHelper( rightHead, rightTreeSize )

        root.left  = leftRoot
        root.right = rightRoot

        return (root, currNode)



    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # determine length of linked list
        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        # do the recursion now
        (root, _dummy) = self.sortedListToBSTHelper( head, length )

        assert _dummy is None

        return root