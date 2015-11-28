class Solution(object):
    
    def is_valid_subnet(self, s):
        return (0 <= int(s) <= 255) and not ( s[0] == '0' and len(s) > 1)
    
    def restoreIpAddressesHelper(self, s, level):
        if level == 0:
            if self.is_valid_subnet(s):
                return [[int(s)]]
            else:
                return [[-1]]

        res = [ [int(s[:i])] + subnet 
                for i in range(1, min(4, len(s)))
                if self.is_valid_subnet(s[:i])
                for subnet in self.restoreIpAddressesHelper(s[i:], level - 1) ]
                
        return res
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = [ '.'.join(map(str, address)) for address in self.restoreIpAddressesHelper(s, 3) 
                                            if all([subnet != -1 for subnet in address])]
        return res