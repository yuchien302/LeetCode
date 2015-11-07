from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = defaultdict(list)
        for str in strs:
            dict[''.join(sorted(str))].append(str)
            
        return [sorted(v) for v in dict.values()]
