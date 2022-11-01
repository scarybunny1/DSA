# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        connected = 0
        component = 0
        curr = head
        while curr:
            if curr.val in s:
                component = 1
            else:
                connected += component
                component = 0
                
            curr = curr.next
        
        return connected + component