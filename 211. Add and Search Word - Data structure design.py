class TrieNode(object):
    def __init__(self):
        self.isEnd = False  # whether this node is an end of a word
        self.children = dict()  # map a char to the child node

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()

            currNode = currNode.children[c]

        currNode.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        currLevelNodes = [self.root]

        for c in word:
            nextLevelNodes = []

            if c=='.':
                for node in currLevelNodes:
                    nextLevelNodes.extend( node.children.values() )
            else:
                for node in currLevelNodes:
                    if c in node.children:
                        nextLevelNodes.append( node.children[c] )

            if not nextLevelNodes:
                return False

            currLevelNodes = nextLevelNodes

        for node in currLevelNodes:
            if node.isEnd:
                return True

        return False



# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")