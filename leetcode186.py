class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        if len(s) == 0: return
        s[:] = ' '.join(reversed(''.join(s).split(' ')))
