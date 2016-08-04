class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a*x**2 + b*x + c

        def fp(x):
            return 2*a*x + b

        list1 = []
        list2 = []

        for num in nums:
            if fp(num) >= 0:
                list2.append(f(num))
            else:
                list1.append(f(num))

        list1.reverse()

        ret = []
        p1, p2 = 0, 0

        while len(ret) < len(nums):
            if p1<len(list1) and (p2==len(list2) or list1[p1]<list2[p2]):
                ret.append(list1[p1])
                p1 += 1
            else:
                ret.append(list2[p2])
                p2 += 1

        return ret