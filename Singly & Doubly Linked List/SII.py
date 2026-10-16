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
        if position < 0:
            return

        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            return

        new_node.next = current.next
        current.next = new_node
    
    def delete(self, val):
        if self.head is None:
            print("Node not found")
            return
        if self.head.val == val:
            self.head = self.head.next
        else:
            current = self.head
            while current is not None:
                
                




s = SinglyList()
for i in range(0, 11):
    s.append(i)
s.insert(3, 5)
s.traversal()