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
    
    def insert_at_last(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next

    def insert_between(self, val, pos):
        if pos == 0:
            self.insert_at_head(val)
            return
        if self.head is None:
            return
        new_node = Node(val)
        current = self.head
        count = 0
        while current.next is not None and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Your position is out of bound")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        

    def delete_head(self, val):
        if self.head is None:
            print("Oops! Your list is empty.")
            return

        if self.head.val == val:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
            return



    def delete_lastNode(self, val):
        if self.head is None:
            print("Oops! Your list is empty.")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        if current.val == val:
            if current.prev is not None:
                current.prev.next = None
            else:
                self.head = None

        
    def deleteInBetween(self, val):
        if self.head is None:
            print("Opps! Your list is empty. ")
            return
        if self.head.val == val:
            self.delete_head(val)
            return
                
        current = self.head
        while current.next is not None:
            current = current.next
            if current.val == val:
                if current.next is not None:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return
                if current.next is None:
                    self.delete_lastNode(val)
                    return

        
        
  
            
d = DoublyLinkedList()

d.insert_at_head(10)
d.insert_at_head(9)
d.insert_at_head(8)
d.insert_at_last(12)
d.insert_between(11, 3)
d.deleteInBetween(11)

d.traversal()
