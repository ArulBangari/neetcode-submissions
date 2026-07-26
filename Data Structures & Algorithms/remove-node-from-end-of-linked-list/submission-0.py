# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = head
        for i in range(n):
            k = k.next
        if not k:
            return head.next
        start = head
        while k.next:
            start = start.next
            k = k.next
        start.next = start.next.next
        return head