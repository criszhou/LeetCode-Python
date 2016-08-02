class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return

        # move nums1 to the back
        for i in range(m-1,-1,-1):
            nums1[i+n] = nums1[i]

        read1 = n
        read2 = 0
        write = 0

        while write < m+n:
            if read1<m+n and (read2==n or nums1[read1]<nums2[read2]):
                nums1[write] = nums1[read1]
                read1 += 1
                write += 1
            else:
                nums1[write] = nums2[read2]
                read2 += 1
                write += 1