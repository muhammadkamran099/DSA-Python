class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def oddEvenList(head):
    if head is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = even_head
    return head
    
def traversal(head):
        if head is None:
            print("Oops! Your Linked List is empty.")
            return

        current = head

        while current is not None:
            print(current.val, end=" ")
            current = current.next
    


head = Node(8)
head.next = Node(7)
head.next.next = Node(1)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(9)

oddEvenList(head)
traversal(head)

