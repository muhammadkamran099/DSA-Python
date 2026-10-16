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
        


s = SinglyList()
for i in range(0, 6):
    s.append(i)