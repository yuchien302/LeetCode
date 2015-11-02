class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i, t in enumerate(tokens):
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                stack.append(-stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                sign = -1 if a * b < 0 else 1
                stack.append( sign * (abs(b) // abs(a)) )
            else:
                stack.append(int(t))
        return stack[-1]
            