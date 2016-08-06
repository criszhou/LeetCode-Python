# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def knows(self, a, b, cache):
        cacheKey = (a,b)

        if cacheKey not in cache:
            cache[cacheKey] = knows(a,b)

        return cache[cacheKey]

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        cache = dict()

        for person in range(1,n):
            if self.knows(candidate, person, cache):
                candidate = person

        if all( ( self.knows(person, candidate, cache) and not self.knows(candidate, person, cache) )
                for person in range(0,n) if person != candidate ):
            return candidate
        else:
            return -1