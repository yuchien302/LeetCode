class Solution(object):
    def diffWaysToCompute(self, input, mem = {}):
        """
        :type input: str
        :rtype: List[int]
        """
        if input in mem:
            return mem[input]
            
        res = []
        if input.isdigit():
            return [int(input)]
        for i in range(1, len(input)-1):
            if input[i] in "+-*":
                res.extend([ self.calc(p, q, input[i]) for p in self.diffWaysToCompute(input[:i], mem) 
                                 for q in self.diffWaysToCompute(input[i+1:], mem)])
        mem[input] = res
        return res
        
    def calc(self, p, q, oper):
        if oper == '-':
            return p-q
        elif oper == '+':
            return p+q
        else:
            return p*q