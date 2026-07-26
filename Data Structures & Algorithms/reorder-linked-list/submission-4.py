# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        while f and f.next:
            f = f.next.next
            s = s.next
        
        prev, s.next = s.next, None
        s, prev = prev, None

        while s:
            tmp = s.next
            s.next = prev
            prev = s
            s = tmp
        s = prev
        f = head
        while s:
            t1, t2 = f.next, s.next
            f.next, s.next = s, t1
            f, s = t1, t2