# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeavesHelper(self, root, results):
        """
        push root and all descendants to results
        return the distance from root to farthest leaf
        """
        if not root:
            return -1

        ret = 1 + max(self.findLeavesHelper(child, results) for child in (root.left, root.right))

        if ret >= len(results):
            results.append([])

        results[ret].append(root.val)

        return ret

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.findLeavesHelper(root, ret)
        return ret
