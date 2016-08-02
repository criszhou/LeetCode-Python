class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        size1 = (C - A) * (D - B)
        size2 = (G - E) * (H - F)

        ovlX = min(C, G) - max(A, E)
        ovlY = min(D, H) - max(B, F)

        sizeOvl = ovlX * ovlY if ovlX > 0 and ovlY > 0 else 0

        return size1 + size2 - sizeOvl