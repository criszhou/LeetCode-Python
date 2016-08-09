# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    BSTcache = [[None]]

    def copyTree(self, root, to_add):
        if not root:
            return None

        ret = TreeNode(root.val + to_add)
        ret.left = self.copyTree(root.left, to_add)
        ret.right = self.copyTree(root.right, to_add)

        return ret

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []

        BSTcache = self.BSTcache

        while n >= len(BSTcache):
            m = len(BSTcache)
            cache_m = []

            for left_tree_size in range(m - 1 + 1):
                right_tree_size = m - 1 - left_tree_size
                # print left_tree_size, right_tree_size

                for left_tree in BSTcache[left_tree_size]:
                    for right_tree in BSTcache[right_tree_size]:
                        new_tree = TreeNode(left_tree_size + 1)
                        new_tree.left = left_tree
                        new_tree.right = self.copyTree(right_tree, left_tree_size + 1)

                        cache_m.append(new_tree)

            BSTcache.append(cache_m)

        return BSTcache[n]

