class Node:
    def __init__(self, val):
        self.val = val
        self.next = None               
   

def detectCycle(head):
    slow = head
    fast = head
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def traversal(head):
        if head is None:
            print("Oops! Your Linked List is empty.")
            return

        current = head

        while current is not None:
            print(current.val, end=" ")
            current = current.next
    


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(detectCycle(head))
traversal(head)

