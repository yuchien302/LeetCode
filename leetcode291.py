class Solution(object):
    def wordPatternMatchHelper(self, pattern, s, dict, words):
        if pattern == "" and s == "":
            return True
        elif pattern == "" or s == "":
            return False
        elif pattern[0] in dict:
            if not s.startswith(dict[pattern[0]]):
                return False
            else:
                return self.wordPatternMatchHelper(pattern[1:], s[len(dict[pattern[0]]):], dict, words)
        else:
            for i in range(1, len(s)+1):
                if s[:i] not in words:
                    dict[pattern[0]] = s[:i]
                    words.add(s[:i])
                    if self.wordPatternMatchHelper(pattern[1:], s[len(dict[pattern[0]]):], dict, words):
                        return True
                    else:
                        words.remove(s[:i])
                        del dict[pattern[0]]
        return False
                
    
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict = {}
        words = set()
        return self.wordPatternMatchHelper(pattern, s, dict, words)
        