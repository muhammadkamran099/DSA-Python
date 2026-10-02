class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyList:
    
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def traversal(self):
        if self.head is None:
            print("Linked List is empty! ")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
                
