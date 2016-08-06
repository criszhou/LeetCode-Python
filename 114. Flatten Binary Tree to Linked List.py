# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flattenHelper(self, root):
        """
        return a the tail
        """
        assert root is not None

        tail = root

        LC, RC = root.left, root.right
        root.left, root.right = None, None

        if LC:
            thisTail = self.flattenHelper( LC )
            tail.right = LC
            tail = thisTail

        if RC:
            thisTail = self.flattenHelper( RC )
            tail.right = RC
            tail = thisTail

        return tail


    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flattenHelper( root )

