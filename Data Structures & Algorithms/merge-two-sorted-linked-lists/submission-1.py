# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                pre = ListNode(list1.val, pre)
                list1 = list1.next
            else:
                pre = ListNode(list2.val, pre)
                list2 = list2.next
        while list1 is not None:
            pre = ListNode(list1.val, pre)
            list1 = list1.next
        while list2 is not None:
            pre = ListNode(list2.val, pre)
            list2 = list2.next
        
        output = None
        while pre is not None:
            output = ListNode(pre.val, output)
            pre = pre.next
        return output
        