# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = [] # each item here is a pair (node, LR),
                        # where LR is "L" or "R", indicating whether it's a left or right child of parent

        stack = self.stack

        if root is not None:
            stack.append( (root,None) )

            while stack[-1][0].left:
                stack.append( (stack[-1][0].left, 'L') )

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)

    def next(self):
        """
        :rtype: int
        """
        stack = self.stack
        ret = stack[-1][0].val

        if stack[-1][0].right is not None:
            # current node has right child, so move there and go left
            stack.append((stack[-1][0].right, 'R'))
            while stack[-1][0].left:
                stack.append( (stack[-1][0].left, 'L') )
        else:
            # current node has no right child, so move up until some node is left child
            while stack and stack[-1][1]=='R':
                stack.pop()
            stack.pop()

        return ret

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())