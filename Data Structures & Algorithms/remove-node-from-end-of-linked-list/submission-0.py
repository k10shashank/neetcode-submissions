# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        for _ in range(n):
            p2 = p2.next
        if p2 is None:
            return p1.next
        else:
            while p2.next is not None:
                p1 = p1.next
                p2 = p2.next
            p1.next = p1.next.next
        return head
        