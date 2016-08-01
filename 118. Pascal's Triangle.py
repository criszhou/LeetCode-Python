class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []

        ret = [[1]]
        while len(ret) < numRows:
            lastRow = ret[-1]

            newRow = [1]
            for i in range(1,len(lastRow)):
                newRow.append(lastRow[i] + lastRow[i-1])
            newRow.append(1)

            ret.append( newRow )

        return ret