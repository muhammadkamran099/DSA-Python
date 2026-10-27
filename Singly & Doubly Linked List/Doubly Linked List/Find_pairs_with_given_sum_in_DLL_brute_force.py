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

    def pairSum(self, target):
        if self.head is None:
            print("List is empty. ")
            return
        temp1 = self.head
        result = []
        while temp1 is not None:
            temp2 = temp1.next
            while temp2 is not None:
                if temp1.val + temp2.val == target:
                    result.append([temp1.val, temp2.val])
                temp2 = temp2.next
            temp1 = temp1.next
        return result



d = DoublyLinkedList()

d.insert_at_head(2)
d.insert_at_head(1)
d.insert_at_last(4)
d.insert_at_last(5)
d.insert_at_last(6)
d.insert_at_last(8)

print(d.pairSum(7))



d.traversal()