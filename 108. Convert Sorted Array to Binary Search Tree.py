# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBSTHelper(self, nums, first, last):
        if first>last:
            return None

        mid = (first + last)//2
        
        ret = TreeNode(nums[mid])
        ret.left  = self.sortedArrayToBSTHelper( nums, first, mid-1 )
        ret.right = self.sortedArrayToBSTHelper( nums, mid+1, last  )

        return ret

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTHelper(nums, first=0, last=len(nums)-1)