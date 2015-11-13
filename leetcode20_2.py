class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_s = []
        dict = {'(':')', '[':']', '{':'}'}
        for ch in s:
            if ch in "([{":
                open_s.append(ch)
            elif not open_s or ch != dict[open_s.pop()]:
                return False

        return len(open_s) == 0