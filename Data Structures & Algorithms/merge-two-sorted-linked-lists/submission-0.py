# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        if list1==None:
            return list2
        if list2==None:
            return list1
                    
        newHead = ListNode(list1.val) if list1.val < list2.val else ListNode(list2.val)
        cur = newHead
        if cur.val == list1.val:
            cur1 = list1.next
            cur2 = list2
        else:
            cur2 = list2.next
            cur1 = list1

        while cur1!=None and cur2!=None:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 =cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur =cur.next
        if cur1!=None:
            cur.next=cur1    
        if cur2!=None:
            cur.next=cur2      
        return newHead            
        