# 1->2->3->4   to  1->4->2->3

class solution:
    def reorderList(self, head: ListNode)  -> None:
        if not head:
            return None
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse second half
        second = slow.next
        prev = slow.next = None
        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        #merge two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
            
            