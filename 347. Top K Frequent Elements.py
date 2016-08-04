from collections import Counter
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numsCounter = Counter(nums)

        CountToNums = defaultdict(list)
        for num, count in numsCounter.items():
            CountToNums[count].append(num)

        ret = []
        for count in range(len(nums), -1, -1):
            if len(ret) < k:
                ret.extend(CountToNums[count])
            else:
                break

        return ret

