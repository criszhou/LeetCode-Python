from operator import xor

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        XOR = reduce( xor, nums )

        bit = ( (XOR ^ (XOR-1)) >> 1 ) + 1

        A = reduce( xor, ( num for num in nums if (num&bit) ) )
        B = XOR ^ A

        return A,B