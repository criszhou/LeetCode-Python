# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbersHelper(self, root, partial, res):
        """
        partial is a number, before comming to this level
        res is a list of one number. We will update that number
        """
        if root is None:
            return

        if root.left is None and root.right is None:
            res[0] += partial * 10 + root.val
            return

        self.sumNumbersHelper(root.left, partial * 10 + root.val, res)
        self.sumNumbersHelper(root.right, partial * 10 + root.val, res)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.sumNumbersHelper(root, partial=0, res=res)
        return res[0]