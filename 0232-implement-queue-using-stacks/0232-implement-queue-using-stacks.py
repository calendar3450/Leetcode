from collections import deque

class MyQueue:

    def __init__(self):
        self.input= deque()

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        n = self.input.popleft()
        return n

    def peek(self) -> int:
        return self.input[0]

    def empty(self) -> bool:
        if self.input:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()