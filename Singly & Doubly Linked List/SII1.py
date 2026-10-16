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
            while current is not None:
                if count == position:
                    new_node.next = current.next
                    current = new_node
                    return
                count += 1
                current = current.next
            
                    
        


s = SinglyList()
for i in range(3, 6):
    s.append(i)
s.insert(0, 8)
s.traversal()