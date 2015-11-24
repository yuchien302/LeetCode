class Solution(object):
    def valid_str(self, str):
        if len(str) > 1 and str[0] == '0':
            return False
        return True
        
    def helper(self, prev, target, remain):
        # print(prev, target, remain)
        if not self.valid_str(prev):
            return False
        if target == remain:
            return True
        elif remain.startswith(target):
            return self.helper(target, str(int(prev) + int(target)), remain[len(target):])
        else:
            return False
        
        
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        N = len(num)
        return any([ self.helper( num[i:j], str(int(num[:i]) + int(num[i:j])), num[j:] )
                     for i in range(1,(N//2)+1)
                     for j in range(i+1,N)
                     if self.valid_str(num[:i]) ])
                     
                     