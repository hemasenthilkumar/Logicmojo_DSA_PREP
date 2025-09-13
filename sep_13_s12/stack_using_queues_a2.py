# push heavy operation

from collections import deque
# push heavy operation
# pop using O(1)
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            val = self.queue.popleft()
            self.queue.append(val)

    def pop(self) -> int:
        return self.queue.popleft() if self.empty() is False else None

    def top(self) -> int:
        return self.queue[0] if self.empty() is False else None

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()