class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop(self):
        if self.head is None:
            print("Queue is empty.")
            return None

        removed = self.head.val
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

        return removed

    def front(self):
        if self.head is None:
            return None
        return self.head.val

    def rear(self):
        if self.tail is None:
            return None
        return self.tail.val

    def display(self):
        current = self.head

        while current:
            print(current.val, end=" <-> ")
            current = current.next

        print("None")


q = Queue()

q.push(4)
q.push(3)
q.push(2)
q.push(1)

q.display()

print("Removed:", q.pop())
print("Front:", q.front())
print("Rear:", q.rear())

q.display()