# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from collections import defaultdict

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        vPosToVals = defaultdict(list)

        leftMost  = 0   # the known minimum vertical position
        rightMost = -1  # the known maximum vertical position

        queue = deque() # each item is a pair (node, verticalPosition)
        if root:
            queue.append( (root,0) )
            leftMost = 0
            rightMost = 0

        while queue:
            node, vPos = queue.popleft()
            vPosToVals[vPos].append( node.val )

            if node.left:
                queue.append( (node.left, vPos-1) )
                leftMost = min(leftMost, vPos-1)
            if node.right:
                queue.append( (node.right, vPos+1) )
                rightMost = max(rightMost, vPos+1)

        ret = []
        for pos in range(leftMost, rightMost+1):
            ret.append( vPosToVals[pos] )

        return ret
