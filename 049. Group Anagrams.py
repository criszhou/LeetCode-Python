class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        retDict = defaultdict(list)  # key is string's representation, value is list of strings with this representation
        for s in strs:
            retDict["".join(sorted(s))].append(s)

        return list(retDict.values())