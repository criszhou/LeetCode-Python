# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMirrorImage(self, root1, root2):
        if root1 is None or root2 is None:
            return root1==root2

        return root1.val==root2.val and self.isMirrorImage(root1.left, root2.right) and self.isMirrorImage(root1.right, root2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root is None or self.isMirrorImage(root.left, root.right)