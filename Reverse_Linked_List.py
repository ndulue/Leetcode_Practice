class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        if not head:
            return None
        
        if head.next is None:
            return head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev