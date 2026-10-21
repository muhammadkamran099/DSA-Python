class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def middleNode(head):
    fast = head
    low = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        low = low.next

    return low


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

middle = middleNode(head)
print(middle.val if middle else None)
