class Solution(object):
    def getGroup(self, x, groupMap):
        ret = x
        while groupMap[ret] != ret:
            ret = groupMap[ret]

        while x != ret:
            nextX = groupMap[x]
            groupMap[x] = ret
            x = nextX

        return ret

    def mergeGroups(self, x, y, groupMap):
        xGroup = self.getGroup(x, groupMap)
        yGroup = self.getGroup(y, groupMap)
        groupMap[xGroup] = yGroup

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False

        groupMap = [ x for x in range(n) ]

        for (x,y) in edges:
            self.mergeGroups(x, y, groupMap)

        groups = { self.getGroup(x, groupMap) for x in range(n) }
        return len(groups) == 1