# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        pnt = output
        while l1 is not None and l2 is not None:
            pnt.val = l1.val + l2.val
            if l1.next is not None or l2.next is not None:
                pnt.next = ListNode()
            pnt = pnt.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            pnt.val = l1.val
            if l1.next is not None:
                pnt.next = ListNode()
            pnt = pnt.next
            l1 = l1.next
        while l2 is not None:
            pnt.val = l2.val
            if l2.next is not None:
                pnt.next = ListNode()
            pnt = pnt.next
            l2 = l2.next
        
        pnt = output
        while pnt is not None:
            if pnt.val >= 10:
                pnt.val = pnt.val - 10
                if pnt.next is not None:
                    pnt.next.val = pnt.next.val + 1
                else:
                    pnt.next = ListNode(1)
            pnt = pnt.next
        
        return output


def executeCarry(arr: Optional[ListNode]):
    pnt = arr
    while pnt is not None:
        if pnt.val >= 10:
            pnt.val = pnt.val - 10
            if pnt.next is None:
                pnt.next = ListNode(1)
            else:
                pnt.next.val = pnt.next.val + 1
    return pnt
        