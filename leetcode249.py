from collections import defaultdict
class Solution(object):
    def fmap(self, string):
        return tuple(map(lambda ch: (ord(ch) - ord(string[0])) % 26, string))
            
        
        
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dict = defaultdict(list)
        for s in strings:
            dict[self.fmap(s)].append(s)
        return [ sorted(d) for d in dict.values() ]