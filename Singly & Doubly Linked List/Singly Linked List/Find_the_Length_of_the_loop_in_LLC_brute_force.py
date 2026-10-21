class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def detectCycle(head):
    temp = head
    my_set = set()
    while temp is not None:
        if temp in my_set:
            count = 1
            current = temp
            temp = temp.next
            while temp != current:
                temp = temp.next
                count += 1
            return count
        my_set.add(temp)
        temp = temp.next
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

