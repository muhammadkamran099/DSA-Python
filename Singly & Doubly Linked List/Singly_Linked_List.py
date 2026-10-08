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
            print("Oops! Your Linked List is empty.")
            return

        current = self.head

        while current is not None:
            print(current.val, end=" ")
            current = current.next

    def insert_at(self, val, position):
        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        count = 0

        while current is not None and count < position:
            prev = current
            current = current.next
            count += 1

        if prev is None:
            return

        prev.next = new_node
        new_node.next = current

    def delete(self, val):
        if self.head is None:
            print("Node not found")
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        prev = None
        current = self.head

        while current is not None:
            if current.val == val:
                prev.next = current.next
                return

            prev = current
            current = current.next

        print("Node not found")


s1 = SinglyList()

s1.append(8)
s1.append(7)
s1.append(3)
s1.insert_at(1, 3)

s1.delete(7)

s1.traversal()
