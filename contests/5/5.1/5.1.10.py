class Stack:
    def __init__(self):
        self.list = []


    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop(-1)

    def is_empty(self):
        return len(self.list) == 0


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")