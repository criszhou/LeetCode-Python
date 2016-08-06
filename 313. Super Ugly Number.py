from heapq import heappop, heappush

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        n -= 1

        SUNs = [1] # super ugly numbers

        heap = [ (p, p, 0) for p in primes ] # each item is a 3-tuple (SUN, p, idx)
        # SUN is super ugly numbers to be added to SUNs, and SUN == p * SUNs[idx]

        while n >= len(SUNs):
            nextSUN, p, SUNidx = heappop( heap )

            if nextSUN > SUNs[-1]:
                SUNs.append( nextSUN )

            SUNidx += 1
            nextSUN = p * SUNs[ SUNidx ]
            heappush( heap, (nextSUN, p, SUNidx) )

        return SUNs[n]