class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        
        isNewMin = len(self.min_stack) == 0 or val <= self.getMin()
        
        if isNewMin:
            self.min_stack.append(val)

    def pop(self):
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
