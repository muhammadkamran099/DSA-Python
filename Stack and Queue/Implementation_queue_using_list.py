class Queue:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.items:
            print("Your queue is empty")
            return None
        return self.items.pop(0)

    def front(self):
        if not self.items:
            return None
        return self.items[0]

    def rear(self):
        if not self.items:
            return None
        return self.items[-1]


q = Queue()

q.push(4)
q.push(3)
q.push(2)
q.push(1)

print(q.items)
print(q.pop())
print(q.pop())
print(q.front())
print(q.rear())