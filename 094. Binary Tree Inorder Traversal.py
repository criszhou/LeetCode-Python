# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [[root, False]]  # each item is a list [node, leftHandled]
        ret = []

        while stack:
            [node, leftHandled] = stack[-1]
            if not leftHandled and node.left:
                stack[-1][1] = True
                stack.append([node.left, False])
            else:
                ret.append(node.val)
                stack.pop()
                if node.right:
                    stack.append([node.right, False])

        return ret