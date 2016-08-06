class Solution(object):
    def findKthLargestHelper(self, nums, k, begin, end):
        """
        quick select
        nums should be viewed as nums[begin:end]
        We want to find nums[begin:end][k] as if nums[begin:end] is sorted
        """

        assert 0 <= k < end - begin

        if end - begin == 1:
            return nums[begin]

        if end - begin == 2:
            if nums[begin] > nums[begin + 1]:
                nums[begin], nums[begin + 1] = nums[begin + 1], nums[begin]
            return nums[begin + k]

        mid = (begin + end - 1) // 2
        midPivot = sorted([nums[begin], nums[end - 1], nums[mid]])[1]
        if nums[begin] == midPivot:
            nums[begin], nums[end - 1] = nums[end - 1], nums[begin]
        elif nums[mid] == midPivot:
            nums[mid], nums[end - 1] = nums[end - 1], nums[mid]

        pivot = nums[end - 1]

        p1, p2 = begin, end - 2
        while p1 < p2:
            if nums[p1] <= pivot:
                p1 += 1
            elif nums[p2] >= pivot:
                p2 -= 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]

        assert p1 == p2
        pivotLoc = p1 if nums[p1] >= pivot else p1 + 1
        nums[pivotLoc], nums[end - 1] = nums[end - 1], nums[pivotLoc]

        if begin + k == pivotLoc:
            return pivot
        elif begin + k < pivotLoc:
            return self.findKthLargestHelper(nums, k, begin, pivotLoc)
        elif begin + k > pivotLoc:
            return self.findKthLargestHelper(nums, k - (pivotLoc + 1 - begin), pivotLoc + 1, end)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        return self.findKthLargestHelper(nums, k, begin=0, end=len(nums))
