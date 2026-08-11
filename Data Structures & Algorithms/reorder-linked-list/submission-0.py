# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None:
            return
        else:
            sec = head.next
            sec_last = head
            last = head.next
            while last.next is not None:
                sec_last = last
                last = last.next
            sec_last.next = None
            head.next = last
            self.reorderList(sec)
            head.next.next = sec #self.reorderList(sec)
        