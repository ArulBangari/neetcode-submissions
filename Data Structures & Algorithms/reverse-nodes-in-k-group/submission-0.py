# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        while True:
            kth = groupPrev
            c = k
            while c:
                kth = kth.next
                if not kth:
                    return dummy.next
                c -= 1
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next
            hold = curr
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            groupPrev.next = prev
            groupPrev = hold