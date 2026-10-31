class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty.")
            return None

        removed = self.head.val
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        return removed

    def peek(self):
        if self.head is None:
            return None
        return self.head.val

    def display(self):
        current = self.head

        while current:
            print(current.val, end=" <-> ")
            current = current.next

        print("None")


s = Stack()

s.push(4)
s.push(3)
s.push(2)
s.push(1)

s.display()

print("Popped:", s.pop())
print("Top:", s.peek())

s.display()