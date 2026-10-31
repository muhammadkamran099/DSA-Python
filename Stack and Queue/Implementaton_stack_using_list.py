class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if len(self.items) == 0:
            print("Your stack is empty")
            return
        self.items.pop()
    def peek(self):
        if len(self.items) == 0:
            print("Your stack is empty")
            return
        print(self.items[-1])
        
s = Stack()

s.push(4)
s.push(3)
s.push(2)
s.push(1)

print(s.items)

s.pop()
s.pop()

print(s.items)

s.peek()