from collections import defaultdict
import random

class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valList = list()
        self.valToIndices = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = ( val in self.valToIndices )

        self.valToIndices[ val ].add( len(self.valList) )
        self.valList.append( val )


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.valToIndices:
            return False

        if self.valList[-1] == val: # easy case, last one is val, so we simply remove last one
            self.valList.pop()
            self.valToIndices[val].remove( len(self.valList) )
        else:
            # difficult case, last one is not val, so we need to find a index of val, and make that index have lastVal
            lastVal = self.valList.pop()
            self.valToIndices[ lastVal ].remove( len(self.valList) )

            swapIdx = self.valToIndices[ val ].pop()
            self.valList[ swapIdx ] = lastVal
            self.valToIndices[ lastVal ].add( swapIdx )

        if not self.valToIndices[val]:
            del self.valToIndices[ val ]

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice( self.valList )



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()