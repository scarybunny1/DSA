# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, next_head):
        if not head or not head.next or head.next == next_head:
            return head
        
        p = self.reverse(head.next, next_head)
        head.next.next = head
        head.next = None
        return p
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        curr = dummy = ListNode(-1)
        curr.next = head
        i = 0
        prev = dummy
        
        #Find the head of the LL to be reversed, while keeping track of the prev node
        while i < left:
            i += 1
            prev = curr
            curr = curr.next
        start = curr
        
        #Find the next link of the tail of the [left-right] LL
        while i < right:
            i += 1
            curr = curr.next
        end = curr.next
        
        #Join the previous LL with the reversed LL
        prev.next = self.reverse(start, end)
        
        #Join the tail of reversed LL with original LL
        while prev.next:
            prev = prev.next
        prev.next = end
        
        return dummy.next
        