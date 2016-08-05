# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def moveToNext(self, stack):
        ret = stack[-1][0].val

        if stack and stack[-1][0].right:
            stack.append((stack[-1][0].right, 'R'))
            while stack[-1][0].left:
                stack.append( (stack[-1][0].left, 'L') )
        else:
            while stack and stack[-1][1] != 'L':
                stack.pop()
            if stack:
                stack.pop()

        return ret


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [ (root,None) ] # each item is a pair (node, LR), where LR means node is a left or right child

        while stack[-1][0].left:
            stack.append( (stack[-1][0].left, 'L') )

        for i in range(k):
            ret = self.moveToNext( stack )

        return ret