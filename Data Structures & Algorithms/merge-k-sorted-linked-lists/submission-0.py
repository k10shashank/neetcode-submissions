# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for k_list in lists:
            pnt = k_list
            while pnt is not None:
                heapq.heappush(arr, pnt.val)
                pnt = pnt.next

        output = ListNode(-10001)
        pnt = output
        while len(arr) != 0:
            top = heapq.heappop(arr)
            pnt.next = ListNode(top)
            pnt = pnt.next

        return output.next
