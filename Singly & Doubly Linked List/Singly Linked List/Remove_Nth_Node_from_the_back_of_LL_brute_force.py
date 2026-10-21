
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeNthNode(head, n):
    if head is None or n <= 0:
        return head

    count = 0
    temp = head

    while temp is not None:
        count += 1
        temp = temp.next

    if n > count:
        return head

    if n == count:
        return head.next

    current = head

    for i in range(count - n - 1):
        current = current.next

    current.next = current.next.next
    return head


def traversal(head):
    if head is None:
        print("Oops! Your Linked List is empty.")
        return

    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head = removeNthNode(head, 4)
traversal(head)
