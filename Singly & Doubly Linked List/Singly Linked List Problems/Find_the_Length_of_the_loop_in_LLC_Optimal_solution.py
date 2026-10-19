class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def detectCycle(head):
    slow = head
    fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.val
    return None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next = Node(10)
head.next.next.next.next.next.next.next.next.next.next = head.next.next.next

print(detectCycle(head))

