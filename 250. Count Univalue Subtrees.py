# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtreesHelper(self, root):
        """
        return a pair (univalTreeCount, isUnival)
        """
        if root is None:
            return (0,True)

        countL, isUnivalL = self.countUnivalSubtreesHelper(root.left)
        countR, isUnivalR = self.countUnivalSubtreesHelper(root.right)

        univalTreeCount = countL + countR

        isUnival = isUnivalL and isUnivalR \
                   and ( root.left is None or root.val==root.left.val ) \
                   and ( root.right is None or root.val==root.right.val )

        if isUnival:
            univalTreeCount += 1

        return univalTreeCount, isUnival

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        univalTreeCount, isUnival = self.countUnivalSubtreesHelper( root )
        return univalTreeCount