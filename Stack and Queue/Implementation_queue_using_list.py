class Queue:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if len(self.items) == 0:
            print("Your stack is empty")
            return
        self.items.pop(0)
        
    def front(self):
        if len(self.items) == 0:
            print("Your stack is empty")
            return
        print(self.items[0])
        
    def rear(self):
        if len(self.items) == 0:
            print("Your stack is empty")
            return
        print(self.items[-1])
        
q = Queue()

q.push(4)
q.push(3)
q.push(2)
q.push(1)

print(q.items)

q.pop()
q.pop()

print(q.items)

q.front()