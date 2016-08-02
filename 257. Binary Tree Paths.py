# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePathsHelper(self, node, partialList, results):
        partialList.append( str(node.val) )

        if node.left is None and node.right is None:
            results.append( "->".join( partialList ) )

        if node.left:
            self.binaryTreePathsHelper( node.left, partialList=partialList, results=results )

        if node.right:
            self.binaryTreePathsHelper( node.right, partialList=partialList, results=results )

        partialList.pop()

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ret = []
        if root:
            self.binaryTreePathsHelper(root, [], ret)
        return ret