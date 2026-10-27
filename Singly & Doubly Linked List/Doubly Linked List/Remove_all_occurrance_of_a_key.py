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
        
    def remove_key_occurrance(self, key):
        current = self.head

        while current is not None:
            if current.val == key:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next

                if current.next is not None:
                    current.next.prev = current.prev

            current = current.next

        return self.head
                    

    
            

d = DoublyLinkedList()

d.insert_at_head(3)
d.insert_at_head(3)

d.insert_at_last(6)
d.insert_at_last(3)
d.insert_at_last(5)
d.insert_at_last(3)

d.traversal()

d.remove_key_occurrance(3)

d.traversal()