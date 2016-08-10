# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSumHelper(self, root, Sum, partialRes, results):
        if root is None:
            return

        if root.left is None and root.right is None:
            if root.val == Sum:
                results.append( partialRes + [root.val] )
            return

        partialRes.append( root.val )
        self.pathSumHelper(root.left, Sum-root.val, partialRes, results)
        self.pathSumHelper(root.right, Sum-root.val, partialRes, results)
        partialRes.pop()

    def pathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type Sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self.pathSumHelper(root, Sum, partialRes=[], results=ret)
        return ret