class Solution(object):
    def evaluate_one(self, operator, operand):
        oper = operator.pop()
        b = operand.pop()
        a = operand.pop()
        if oper == '+':
            operand.append(a+b)
        else:
            operand.append(a-b)
            
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator = []
        operand = []
        prev_digit = False
        
        for ch in s:
            if ch.isdigit():
                if prev_digit:
                    operand[-1] = operand[-1] * 10 + int(ch)
                else:
                    operand.append(int(ch))
                    prev_digit = True
            else:
                prev_digit = False
            
            if ch in '+-':
                if len(operator) > 0 and operator[-1] in '+-':
                    self.evaluate_one(operator, operand)
                operator.append(ch)
            if ch == ')':
                while operator[-1] != '(':
                    self.evaluate_one(operator, operand)
                operator.pop()
            if ch == '(':
                operator.append(ch)
                
        while len(operator) > 0:
            self.evaluate_one(operator, operand)
                    
        return operand[-1]