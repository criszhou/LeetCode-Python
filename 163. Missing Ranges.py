import itertools

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ret = []

        lastNum = lower-1

        for num in itertools.chain( nums, [upper+1] ):
            if lastNum+2 == num:
                ret.append( str(lastNum+1) )
            elif lastNum+2 < num:
                ret.append( "{}->{}".format( lastNum+1, num-1 ) )

            lastNum = num

        return ret