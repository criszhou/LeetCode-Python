class Solution(object):
    @staticmethod
    def reduceArrays(nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)

        mid1 = len1 // 2
        mid2 = (len2 - 1) // 2

        if nums1[mid1] <= nums2[mid2]:
            nums1 = nums1[mid1:]
            nums2 = nums2[:len2 - mid1]
        elif nums1[mid1] > nums2[mid2]:
            nums1 = nums1[:mid1 + 1]
            nums2 = nums2[len1 - mid1 - 1:]

        return (nums1, nums2)

    @staticmethod
    def isBaseCase(nums1, nums2):
        assert len(nums1) <= len(nums2)
        assert len(nums2) > 0
        return len(nums1) <= 2

    @staticmethod
    def middle2(nums):
        assert len(nums) % 2 == 0
        return (nums[len(nums) // 2], nums[len(nums) // 2 - 1])

    @staticmethod
    def median(nums):
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2] / 1.0
        elif len(nums) % 2 == 0:
            return sum(Solution.middle2(nums)) / 2.0

    def handleBaseCase(self, nums1, nums2):
        assert self.isBaseCase(nums1, nums2)

        if len(nums1) == 0:
            return self.median(nums2)

        if len(nums1) == 1 and len(nums2) % 2 == 0:
            print(nums1 + list(self.middle2(nums2)))
            return self.median(sorted(nums1 + list(self.middle2(nums2))))

        return self.median(sorted(nums1 + nums2))

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # Since now, nums1 is shorter than nums2, or same length

        while not self.isBaseCase(nums1, nums2):
            nums1, nums2 = self.reduceArrays(nums1, nums2)

        return self.handleBaseCase(nums1, nums2)