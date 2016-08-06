class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        L, R = 0, len(height)-1

        while L<R:
            HL = height[L]
            HR = height[R]
            ret = max( ret, (R-L) * min(HL, HR) )

            if HL <= HR:
                L += 1

            if HL >= HR:
                R -= 1

        return ret