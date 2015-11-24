import re
class Solution(object):
    def is_valid(self, s):
        s = re.sub('\w', '', s)
        while s.find('()') != -1:
            s = s.replace('()', '')
        return s == ""

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        memo = set()
        if self.is_valid(s):
            return [s]
        queue = [s]
        while all([not self.is_valid(p) for p in queue]):
            temp_queue = []
            for p in queue:
                for i in range(len(p)):
                    if not p[i].isalpha() and (p[:i]+p[i+1:]) not in memo:
                        temp_queue.append(p[:i]+p[i+1:])
                        memo.add((p[:i]+p[i+1:]))
            queue = temp_queue

        res = [p for p in queue if self.is_valid(p)]
        return res

        