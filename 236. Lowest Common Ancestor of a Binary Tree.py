# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestorHelper(self, root, p, q):
        """
        Return a tuple (commonAncestor, pFound, qFound)
        if not both pFound and qFound, commonAncestor is None
        """
        assert p != q

        if root is None:
            return (None, False, False)

        pFound = (root==p)
        qFound = (root==q)

        (leftCommonAncestor, leftPFound, leftQFound) = self.lowestCommonAncestorHelper(root.left, p, q)
        if leftCommonAncestor:
            assert leftPFound and leftQFound
            return (leftCommonAncestor, True, True)

        pFound = pFound or leftPFound
        qFound = qFound or leftQFound
        if pFound and qFound:
            return (root, True, True)

        (rightCommonAncestor, rightPFound, rightQFound) = self.lowestCommonAncestorHelper(root.right, p, q)
        if rightCommonAncestor:
            assert rightPFound and rightQFound
            return (rightCommonAncestor, True, True)

        pFound = pFound or rightPFound
        qFound = qFound or rightQFound
        if pFound and qFound:
            return (root, True, True)

        return (None, pFound, qFound)


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p==q:
            return p

        if root in (p,q):
            return root

        (ret, pFound, qFound) = self.lowestCommonAncestorHelper(root, p, q)
        assert pFound and qFound
        return ret