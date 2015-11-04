class Solution(object):
    def generate_with_open_close(self, o, c):
        res = []
        if c == 0:
            return [""]
            
        if o == c or 0 < o:
            res.extend(map(lambda s: '(' + s , self.generate_with_open_close(o-1, c)))
            
        if o < c:
            res.extend(map(lambda s: ')' + s , self.generate_with_open_close(o, c-1)))
        
        return res
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        return self.generate_with_open_close(n, n)
        