# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        o = head
        e = head.next
        eH = e
        
        while e != None and e.next != None:
            o.next = o.next.next
            e.next = e.next.next
            
            o = o.next
            e = e.next
        o.next = eH
        return head