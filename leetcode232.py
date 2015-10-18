class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack0 = []
        self.stack1 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack0.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack1) == 0:
            while len(self.stack0) != 0:
                self.stack1.append(self.stack0.pop())
        self.stack1.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack1) == 0:
            while len(self.stack0) != 0:
                self.stack1.append(self.stack0.pop())
                
        return self.stack1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack0) == 0 and len(self.stack1) == 0
        