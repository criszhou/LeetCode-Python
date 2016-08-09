# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTreeHelper(self,
                        inorder,   ioBegin, ioEnd,
                        postorder, poBegin, poEnd,
                        inorderValToIndex):
        assert ioEnd-ioBegin == poEnd-poBegin

        if ioEnd == ioBegin:
            return None
        if ioEnd == ioBegin + 1:
            return TreeNode( inorder[ioBegin] )

        rootVal = postorder[poEnd-1]
        ret = TreeNode(rootVal)
        ioRootValIdx = inorderValToIndex[ rootVal ]

        ret.left  = self.buildTreeHelper(inorder=inorder,     ioBegin=ioBegin, ioEnd=ioRootValIdx,
                                         postorder=postorder, poBegin=poBegin, poEnd=poBegin+ioRootValIdx-ioBegin,
                                         inorderValToIndex=inorderValToIndex)
        ret.right = self.buildTreeHelper(inorder=inorder,     ioBegin=ioRootValIdx+1, ioEnd=ioEnd,
                                         postorder=postorder, poBegin=poEnd+ioRootValIdx-ioEnd, poEnd=poEnd-1,
                                         inorderValToIndex=inorderValToIndex)
        return ret

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorderValToIndex = { val:i for i,val in enumerate(inorder) }
        return self.buildTreeHelper(inorder, 0, len(inorder), postorder, 0, len(postorder), inorderValToIndex)