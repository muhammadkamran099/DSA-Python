class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.items:
            print("Stack is empty.")
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


s = Stack()

s.push(4)
s.push(3)
s.push(2)
s.push(1)

print(s.items)

print(s.pop())
print(s.pop())

print(s.items)
print(s.peek())