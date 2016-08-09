# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTreeHelper(self,
                        preorder, poBegin, poEnd,
                        inorder,  ioBegin, ioEnd,
                        inorderValToIndex):
        assert ioEnd-ioBegin == poEnd-poBegin

        if ioEnd == ioBegin:
            return None
        if ioEnd == ioBegin + 1:
            return TreeNode( inorder[ioBegin] )

        rootVal = preorder[poBegin]
        ret = TreeNode(rootVal)
        ioRootValIdx = inorderValToIndex[ rootVal ]

        ret.left  = self.buildTreeHelper(preorder=preorder, poBegin=poBegin+1, poEnd=poBegin+1+ioRootValIdx-ioBegin,
                                         inorder=inorder,   ioBegin=ioBegin, ioEnd=ioRootValIdx,
                                         inorderValToIndex=inorderValToIndex)
        ret.right = self.buildTreeHelper(preorder=preorder, poBegin=poEnd+ioRootValIdx+1-ioEnd, poEnd=poEnd,
                                         inorder=inorder,   ioBegin=ioRootValIdx+1, ioEnd=ioEnd,
                                         inorderValToIndex=inorderValToIndex)
        return ret

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inorderValToIndex = { val:i for i,val in enumerate(inorder) }
        return self.buildTreeHelper(preorder, 0, len(preorder), inorder, 0, len(inorder), inorderValToIndex)
