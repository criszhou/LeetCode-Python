# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        retLevels = []  # list of strings, each string represents a level
        currLevel = [root]

        while currLevel:
            # in each level, write "" as None, and join node vals by ','
            # at the end, join levels by ';'
            currLevelStr = ",".join(str(node.val) if node else "" for node in currLevel)
            retLevels.append(currLevelStr)

            nextLevel = []
            for node in currLevel:
                if node:
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)

            currLevel = nextLevel

        return ";".join(retLevels)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        levelStrs = data.split(";")

        root = TreeNode(int(levelStrs[0]))
        currLevelNodes = [root]  # only contains non-None nodes

        for level in range(1, len(levelStrs)):
            nextLevelNodes = []
            nextLevelVals = levelStrs[level].split(",")

            for i, nodeVal in enumerate(nextLevelVals):
                if nodeVal != "":
                    newNode = TreeNode(int(nodeVal))
                    if i % 2 == 0:
                        currLevelNodes[i // 2].left = newNode
                    else:
                        currLevelNodes[i // 2].right = newNode

                    nextLevelNodes.append(newNode)

            currLevelNodes = nextLevelNodes

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))