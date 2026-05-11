# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head== None:
            return False
        s,f = head,head.next
        while f !=None:
            if f==s:
                return True
            s =s.next
            f= f.next.next if f.next !=None else None
        return f ==s     
        