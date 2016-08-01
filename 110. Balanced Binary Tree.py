# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalancedHelper(self, root):
        """
        return a pair (isBal, depth)
        """
        if root is None:
            return (True, 0)

        leftIsBal, leftDepth = self.isBalancedHelper(root.left)
        if not leftIsBal:
            return (False, 0)

        rightIsBal, rightDepth = self.isBalancedHelper(root.right)

        isBal = leftIsBal and rightIsBal and abs(leftDepth-rightDepth)<=1
        depth = 1 + max(leftDepth, rightDepth)

        return ( isBal, depth )

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isBal, depth = self.isBalancedHelper( root )
        return isBal