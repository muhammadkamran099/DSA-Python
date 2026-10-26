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

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def insert_at_last(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def insert_between(self, val, pos):
        if pos < 0:
            print("Invalid position.")
            return

        if pos == 0:
            self.insert_at_head(val)
            return

        current = self.head
        count = 0

        while current is not None and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position is out of bounds.")
            return

        new_node = Node(val)
        new_node.next = current.next
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node

        current.next = new_node

    def traversal(self):
        current = self.head

        while current is not None:
            print(current.val, end=" ")
            current = current.next

        print()

    def delete_head(self, val):
        if self.head is None:
            print("Oops! Your list is empty.")
            return

        if self.head.val != val:
            print("Value not found at the head.")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def delete_lastNode(self, val):
        if self.head is None:
            print("Oops! Your list is empty.")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        if current.val != val:
            print("Value not found at the last node.")
            return

        if current.prev is None:
            self.head = None
        else:
            current.prev.next = None
    
    
    def delete_in_Between(self, val):
        if self.head is None:
            print("Opps! Your list is empty. ")
            return
    
        if self.head.val == val:
            self.delete_head(val)
            return
        
        current = self.head
        while current is not None and current.val != val:
            current = current.next

        if current is None:
            print("Node not found. ")
            return
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
    
    def insert_in_sorted(self, val, slow, fast):
        new_node = Node(val)
        slow.next = new_node
        new_node.prev = slow
        new_node.next = fast
        fast.prev = new_node
        
    
    def insert_in_sorted_list(self, val):
        if self.head is None:
            print("Opps! your list is empty. ")
            return 
        slow = self.head
        fast = slow.next
        current = self.head
        while current.next is not None:
            if slow.val <= val:
                if fast.val >= val:
                    self.insert_in_sorted(val, slow, fast)
                    return
            slow = slow.next
            fast = fast.next
            current = current.next
        print("No valid place to insert")

        
        
        
            
            

d = DoublyLinkedList()

d.insert_at_head(10)
d.insert_at_head(9)
d.insert_at_head(7)
d.insert_at_last(12)
d.insert_between(11, 3)
d.insert_at_last(12)

d.insert_in_sorted_list(8)


d.delete_in_Between(12)



d.traversal()