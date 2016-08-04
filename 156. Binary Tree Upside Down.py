# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTreeHelper(self, root):
        """
        return a pair, (newRoot, RightmostDescendant)
        """

        if root is None:
            return (None, None)

        if root.left is None:
            assert root.right is None
            return (root, root)

        leftResRoot, leftResRight = self.upsideDownBinaryTreeHelper( root.left )
        leftResRight.left, leftResRight.right = root.right, root
        root.left = None
        root.right = None

        return leftResRoot, root

    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ret, right = self.upsideDownBinaryTreeHelper(root)

        return ret