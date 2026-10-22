class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
            
            
d = DoublyLinkedList()

d.insert_at_head(10)
d.insert_at_head(9)
d.insert_at_head(8)

d.traversal()
