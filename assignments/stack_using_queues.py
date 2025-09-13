from collections import deque
class MyStack:

    # this is pop heavy operation
    # if we need push heavy and pop using o(1), then we need to do the append logic to the push
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue)-1):
            # move all elements behind the last one
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        if self.queue:
            return self.queue[-1]

    def empty(self) -> bool:
        return bool(self.queue) == False