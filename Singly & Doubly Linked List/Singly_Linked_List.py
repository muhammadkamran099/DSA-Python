class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        

node1 = Node(8)
node2 = Node(6)
node3 = Node(4)
node4 = Node(9)
node1.next = node2
node2.next = node3
node3.next = node4

print(node1.next.val)