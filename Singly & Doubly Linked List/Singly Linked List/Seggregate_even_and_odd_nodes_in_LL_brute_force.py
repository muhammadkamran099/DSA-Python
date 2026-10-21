class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def oddEvenList(head):
    if head is None:
        return head
    temp = head
    my_list = []
    
    while temp is not None:
        my_list.append(temp.val)
        if temp.next is None:
            break
        temp = temp.next.next

    temp = head.next
    while temp is not None:
        my_list.append(temp.val)
        if temp.next is None:
            break
        temp = temp.next.next

        
    current = head
    n = len(my_list)
    for i in range(n):
        current.val = my_list[i]
        current = current.next
    
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

