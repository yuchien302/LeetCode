class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p in '([{':
                stack.append(p)
            elif len(stack)==0:
                return False
            elif p == ')' and stack.pop() != '(':
                return False
            elif p == ']' and stack.pop() != '[':
                return False
            elif p == '}' and stack.pop() != '{':
                return False
                
        return len(stack) == 0
        