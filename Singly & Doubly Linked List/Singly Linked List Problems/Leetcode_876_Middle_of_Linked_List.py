class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast = head
        low = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            low = low.next
        return low