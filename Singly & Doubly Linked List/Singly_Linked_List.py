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
            print("Oops! Your Linked List is empty. ")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
                
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current.next is not None and count < position:
                prev = current
                current = current.next
                count += 1
            prev.next = new_node
            new_node.next = current
        
            
    
s1 = SinglyList()
s1.append(8)
s1.append(7)
s1.append(3)
s1.append(2)
s1.insert_at(1, 3)
s1.traversal()
                
