# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutiveHelper(self, root):
        """
        return a pair (longest, longestFromRoot)
        where longest is the longest in this tree, and longestFromRoot requires the path to start from root
        """
        if not root:
            return (0,0)

        longest, longestFromRoot = 1, 1

        if root.left:
            leftLongest, leftLongestFromRoot = self.longestConsecutiveHelper( root.left )
            if root.left.val == root.val + 1:
                longestFromRoot = max( longestFromRoot, leftLongestFromRoot + 1 )
            longest = max( longest, longestFromRoot, leftLongest)

        if root.right:
            rightLongest, rightLongestFromRoot = self.longestConsecutiveHelper( root.right )
            if root.right.val == root.val + 1:
                longestFromRoot = max( longestFromRoot, rightLongestFromRoot + 1 )
            longest = max( longest, longestFromRoot, rightLongest)

        return longest, longestFromRoot


    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest, longestFromRoot = self.longestConsecutiveHelper( root )
        return longest