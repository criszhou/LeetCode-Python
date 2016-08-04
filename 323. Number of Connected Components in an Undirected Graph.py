class Solution(object):
    def getGroup(self, i, groupMap):
        ret = i
        while groupMap[ret] != ret:
            ret = groupMap[ret]

        while groupMap[i] != ret:
            nextI = groupMap[i]
            groupMap[i] = ret
            i = nextI

        return ret

    def merge(self, i, j, groupMap):
        groupI = self.getGroup(i, groupMap)
        groupJ = self.getGroup(j, groupMap)
        groupMap[groupI] = groupJ

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        groupMap = [ i for i in range(n) ]

        for (i,j) in edges:
            self.merge(i,j, groupMap)

        return len( { self.getGroup(i,groupMap) for i in range(n) } )
