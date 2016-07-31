class TwoSum(object):
    def __init__(self):
        """
        initialize your data structure here
        """
        self.numCount = dict()

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.numCount[number] = self.numCount.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.numCount:
            other = value - num
            if other in self.numCount and ( other!=num or self.numCount[num]>1 ):
                return True

        return False



# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)