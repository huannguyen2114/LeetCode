class MinStack:
    # Idea: using monototic stack to keep track of the number which can be popped
    def __init__(self):
        self.st = []
        self.ms = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.ms or self.st[-1] < self.st[self.ms[-1]]:
            self.ms.append(len(self.st) - 1)

    def pop(self) -> None:
        if len(self.st) - 1 == self.ms[-1]:
            self.ms.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.st[self.ms[-1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()