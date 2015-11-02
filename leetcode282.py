class Solution(object):
    
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num == "":
            return []
        strs = [(num[0], num[0], int(num[0]), 0, 1)]
        strs2 = []
        nums = map(int, num)
        for i in range(1, len(num)-1):
            c = num[i]
            n = nums[i]
            for (s0, s00, s1, s2, s3) in strs:
                strs2.append( (s0 + "+" + c, c, s1 + n, int(s1), 1 ) )
                strs2.append( (s0 + "-" + c, c, s1 - n, int(s1), -1 ) )
                strs2.append( (s0 + "*" + c, c, s2 + (s1-s2)*n , s2, (s1-s2) ) )
                if s00[0] != '0':
                    strs2.append( (s0 + c, s00 + c,s2 + (s1-s2)*10 + s3 * n, s2, s3 ))
                
            strs = strs2
            strs2 = []

        c = num[-1]
        for (s0, s00, s1, s2, s3) in strs:
            if s1 + int(c) == target:
                strs2.append( s0 + "+" + c )
                
            if s1 - int(c) == target:
                strs2.append( s0 + "-" + c )
                
            if s2 + (s1-s2)*int(c) == target:
                strs2.append( s0 + "*" + c )
                
            if  s00[0] != '0' and s2 + (s1-s2)*10 + s3 * int(c) == target:
                strs2.append( s0 + c )

        # strs = map(lambda (s0, s00, s1, s2, s3): s0, filter(lambda (s0, s00, s1, s2, s3): s1 == target, strs))
        
        return strs2