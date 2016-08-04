import random

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valToIndex = dict()
        self.valList = list()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.valToIndex:
            return False

        self.valToIndex[val] = len(self.valList)
        self.valList.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.valToIndex:
            return False

        lastVal = self.valList[-1]
        valIndex = self.valToIndex[val]
        if lastVal != val:
            self.valToIndex[lastVal] = valIndex
            self.valList[valIndex] = lastVal

        self.valList.pop()
        self.valToIndex.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice( self.valList )


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.delete(val)
# param_3 = obj.getRandom()