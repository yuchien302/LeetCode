class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0":
            return 0

        decode, delay = 1, 1
        for i in range(1, len(s)):
            new_delay = decode
            new_decode = 0
            
            if 10 <= int(str(s[i-1:i+1])) <= 26:
                new_decode += delay
            
            if s[i] != "0":
                new_decode += decode

            decode, delay = new_decode, new_delay

        return decode
                
