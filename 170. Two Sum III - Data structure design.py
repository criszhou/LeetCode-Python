class TwoSum(object):
    def __init__(self):
        """
        initialize your data structure here
        """
        self.numSet = set()
        self.twiceSet = set()

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.numSet:
            self.twiceSet.add(number)

        self.numSet.add(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        if value%2==0 and value//2 in self.twiceSet:
            return True

        for num in self.numSet:
            if value-num!=num and value-num in self.numSet:
                return True

        return False



# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)