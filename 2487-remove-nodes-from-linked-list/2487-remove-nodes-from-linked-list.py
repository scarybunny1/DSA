# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def f(self, node):
        if not node.next:
            return node
        
        next_node = self.f(node.next)
        node.next = next_node
        if next_node.val > node.val:
            node.next = None
            return next_node
        else:
            return node
        
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.f(head)