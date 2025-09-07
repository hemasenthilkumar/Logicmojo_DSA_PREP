class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, x):
        
        self.stack.append(x)
        top += 1
        
    def pop(self):
        top -= 1
        self.stack.pop()
    
    def top(self):
        return self.stack[self.top]
        
    def isEmpty(self):
        return self.top == -1
        
    def size(self):
        return self.top + 1
    