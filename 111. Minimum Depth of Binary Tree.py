# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        currLevel = 1
        currLevelNodes = [root]

        while currLevelNodes:
            nextLevelNodes = []
            for node in currLevelNodes:
                if node.left is None and node.right is None:
                    return currLevel

                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)

            currLevel += 1
            currLevelNodes = nextLevelNodes