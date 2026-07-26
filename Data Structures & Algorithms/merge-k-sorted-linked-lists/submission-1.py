# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1, head2):
        prev = ListNode()
        prev.next = head1
        hold = prev
        while head1 and head2:
            if head1.val > head2.val:
                prev.next = head2
                head2 = head2.next
                prev = prev.next
                prev.next = head1
            else:
                prev = head1
                head1 = head1.next
        head1 = prev
        if head2:
            head1.next = head2
        head1 = hold.next
        return head1

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i - 1])
        return lists[-1]
            