# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        currLevel = []
        if root:
            currLevel.append(root)

        while currLevel:
            nextLevel = []

            for i,node in enumerate(currLevel):
                node.next = currLevel[i+1] if i+1<len(currLevel) else None

                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )

            currLevel = nextLevel
        