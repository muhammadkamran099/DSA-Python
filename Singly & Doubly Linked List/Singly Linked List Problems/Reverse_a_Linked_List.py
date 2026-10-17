class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def revList(head):
    st = []
    temp = head
    while temp is not None:
        st.append(temp.val)
        temp = temp.next
    current = head
    while current is not None:
        e = st.pop()
        current.val = e
        current = current.next
    
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

revList(head)
traversal(head)
