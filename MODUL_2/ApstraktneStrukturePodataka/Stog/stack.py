class Stack(list):
    def __init__(self):
        super().__init__()
        return
    
    def push(self, e):
        self.append(e)
        return

    def pop(self):
        return super().pop()

    def isEmpty(self):
        return len(self) == 0

s = Stack()

s.push('A')
s.push('B')
s.push('C')

print(s.pop())
print(s.pop())

s.push('D')
print(s.pop())
