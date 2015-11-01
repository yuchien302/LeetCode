class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        
        res += str(numerator // denominator)
        
        repeat = {}
        rem = numerator % denominator
        if rem != 0:
            res += '.'
            
        idx = 0
        while rem != 0 and rem not in repeat:
            repeat[rem] = idx
            idx += 1
            
            rem *= 10
            res += str(rem // denominator)
            rem %= denominator
        
        if rem in repeat:
            idx = len(repeat) - repeat[rem]
            res = res[:-idx] + '(' + res[-idx:] + ')'
            
        
        return res