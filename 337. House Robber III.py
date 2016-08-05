# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def robHelper(self,root):
        """
        return a pair (IncludeRootRes, ExcludeRootRes)
        so global max will be max of those 2
        """
        if not root:
            return (0,0)

        withRootL, noRootL = self.robHelper( root.left  )
        withRootR, noRootR = self.robHelper( root.right )

        includeRootRes = root.val + noRootL + noRootR
        excludeRootRes = max( withRootL, noRootL ) + max( withRootR, noRootR )

        return (includeRootRes, excludeRootRes)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        (includeRootRes, excludeRootRes) = self.robHelper( root )
        return max(includeRootRes, excludeRootRes)