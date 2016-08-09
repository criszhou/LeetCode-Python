from heapq import heappush, heappop

class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1

        UNs = [1]  # super ugly numbers

        heap = [(p, p, 0) for p in [2,3,5]]  # each item is a 3-tuple (UN, p, idx)
        # UN is super ugly numbers to be added to UNs, and UN == p * UNs[idx]

        while n >= len(UNs):
            nextUN, p, UNidx = heappop(heap)
        
            if nextUN > UNs[-1]:
                UNs.append(nextUN)

            UNidx += 1
            nextUN = p * UNs[UNidx]
            heappush(heap, (nextUN, p, UNidx))

        return UNs[n]