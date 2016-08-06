# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        if p.right:
            ret = p.right
            while ret.left:
                ret = ret.left
        else:
            ret = None
            node = root
            while node != p:
                if node.val > p.val:
                    ret = node
                    node = node.left
                else:
                    node = node.right

        return ret