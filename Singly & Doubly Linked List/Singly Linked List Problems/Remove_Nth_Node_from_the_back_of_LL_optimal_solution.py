
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def removeNthNode(head, n):
    if head is None or n <= 0:
        return head

    p1 = head
    p2 = head

    for i in range(n):
        if p1 is None:
            return head
        p1 = p1.next

    if p1 is None:
        return head.next

    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next

    p2.next = p2.next.next
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

removeNthNode(head, 2)
traversal(head)