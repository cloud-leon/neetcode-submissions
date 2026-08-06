# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        l1 = None
        for l2 in lists:
            x = self.mergeLists(l1,l2)
            l1 = x
        return l1
    def mergeLists(self,l1,l2):
        temp = ListNode(0)
        res = temp
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next= l2
                l2 = l2.next
            temp = temp.next
        
        temp.next = l1 if l1 else l2
        return res.next