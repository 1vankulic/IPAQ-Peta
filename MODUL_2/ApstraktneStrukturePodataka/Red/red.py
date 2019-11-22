class Queue(list):
    def __init__(self):
        super().__init__()
        return

    def enqueue(self, e):
        self.append(e)
        return

    def dequeue(self):
        return self.pop(0)

    def isEmpty(self):
        return len(self) == 0

r = Queue()
r.enqueue('A')
r.enqueue('B')
r.enqueue('C')

print(r.dequeue())
print(r.dequeue())
r.enqueue('D')
print(r.dequeue())