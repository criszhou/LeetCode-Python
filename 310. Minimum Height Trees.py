class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodeToNeighbors = { i : set() for i in range(n) }

        for (p,q) in edges:
            nodeToNeighbors[p].add(q)
            nodeToNeighbors[q].add(p)

        leaves = [ i for i in range(n) if len(nodeToNeighbors[i])==1 ]

        while len(nodeToNeighbors)>2:
            newLeaves = []

            for leaf in leaves:
                adj = nodeToNeighbors[leaf].pop() # adj is the node adjacent to this leaf
                nodeToNeighbors[adj].remove( leaf )

                if len(nodeToNeighbors[adj])==1:
                    newLeaves.append( adj )

                del nodeToNeighbors[leaf]

            leaves = newLeaves

        return [ i for i in nodeToNeighbors ]