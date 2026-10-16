class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SinglyList:
    def __init__(self):
        self.head = None
        
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def traversal(self):
        if self.head is None:
            print("Oops! Your list is empty. ")
            return
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
                
    def insert(self, position, val):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            current = self.head
            count = 0
            prev = None
            while current is not None and count < position:
                if count == position:
                    prev.next = new_node
                    new_node.next = current.next
                    return
                count += 1
                prev = current
                current = current.next
                
            
                    
        


s = SinglyList()
for i in range(0, 6):
    s.append(i)
s.insert(3, 8)
s.traversal()