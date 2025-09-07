class MinStack:

    def __init__(self):
            self.stack = []
            self.min_element = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_element = val
            self.stack.append(val)
        elif val <= self.min_element:
            self.stack.append(2*val-self.min_element)
            self.min_element = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            val = self.stack.pop()
            if val <= self.min_element:
                self.min_element = 2*self.min_element - val
            if not self.stack:
                self.min_element = None
        else:
            return None

    def top(self) -> int:
        if not self.stack:
            return None
        if self.stack[-1] <= self.min_element:
            return self.min_element
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()