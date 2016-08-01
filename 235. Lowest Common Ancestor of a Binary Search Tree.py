# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p==q:
            return p

        node = root

        while p!=node and q!=node:
            if (p.val<node.val) != (q.val<node.val):
                return node
            elif p.val>node.val:
                node = node.right
            else:
                node = node.left

        return node