class Queue:
    def __init__(self):
        self.list = []


    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop(0)

    def is_empty(self):
        return len(self.list) == 0


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")