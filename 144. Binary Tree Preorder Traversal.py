# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ret = []
        stack = [root]

        while stack:
            node = stack.pop()
            ret.append( node.val )

            if node.right:
                stack.append( node.right )
            if node.left:
                stack.append( node.left )

        return ret