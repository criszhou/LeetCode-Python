from collections import defaultdict

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        assert len(A[0]) == len(B)

        mapJI = defaultdict(list) # map j to a list of i, where A[i][j] != 0
        mapJK = defaultdict(list) # map j to a list of k, where B[j][k] != 0

        for i,Row in enumerate(A):
            for j,n in enumerate(Row):
                if n!=0:
                    mapJI[j].append( i )

        for j,Row in enumerate(B):
            for k,n in enumerate(Row):
                if n!=0:
                    mapJK[j].append( k )

        ret = [ [0 for k in range(len(B[0]))] for i in range(len(A)) ]

        for j in range(len(B)):
            for i in mapJI[j]:
                for k in mapJK[j]:
                    ret[i][k] += A[i][j] * B[j][k]

        return ret