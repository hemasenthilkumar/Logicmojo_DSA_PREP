class MinStack:
    # TC: O(1)
    # SC: O(N)

    def __init__(self):
        self.stack= []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack: 
            prev_min  = self.min_stack[-1]
            if val < prev_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(prev_min)
        else:
            self.min_stack.append(val)  

    def pop(self) -> None:
        if self.stack and self.min_stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
