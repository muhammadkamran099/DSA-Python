class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class DoublyLinked:
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head =  new_node
        
    def traverse(self):
        if self.head is None:
            print("Oops! Your list is empty. ")
            return
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        
    def insert_at_end(self, val):
        if self.head is None:
            print("Oops! Your list is empty. ")
            return
        new_node = Node(val)
        
        
        
d = DoublyLinked()
d.insert_at_head(8)
d.insert_at_head(7)
d.insert_at_head(6)
d.traverse()