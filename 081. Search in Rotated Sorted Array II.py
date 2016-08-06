from bisect import bisect_left

class Solution(object):
    def searchHelper(self, nums, target, first, last):
        if last-first <= 3:
            return any( nums[x]==target for x in range(first, last+1) )

        if nums[first] < nums[last]:
            pos = bisect_left(nums, target, lo=first, hi=last+1)
            return pos != last+1 and nums[pos]==target

        if target in ( nums[first], nums[last] ):
            return True

        mid = (last+first)//2
        if nums[mid]==target:
            return True

        if nums[last] == nums[first]:
            return self.searchHelper( nums, target, first+1, mid-1 ) or self.searchHelper( nums, target, mid+1, last-1 )

        assert nums[last] < nums[first]

        if nums[mid]<=nums[last]:
            if nums[mid]<target<nums[last]:
                return self.searchHelper(nums, target, mid+1, last-1)
            else:
                return self.searchHelper(nums, target, first+1, mid-1)
        elif nums[mid]>=nums[first]:
            if nums[first]<target<nums[mid]:
                return self.searchHelper(nums, target, first+1, mid-1)
            else:
                return self.searchHelper(nums, target, mid+1, last-1)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.searchHelper( nums, target, first=0, last=len(nums)-1 )