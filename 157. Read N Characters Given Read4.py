# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        write = 0

        tempBuf = [None] * 4
        endReached = False
        while write<n and not endReached:
            thisSize = read4(tempBuf)
            if thisSize<4:
                endReached = True

            for i in range(thisSize):
                buf[write] = tempBuf[i]
                write += 1
                if write==n:
                    break

        return write