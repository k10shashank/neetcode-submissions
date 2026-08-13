import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -i)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            sec = -heapq.heappop(max_heap)
            if first > sec:
                heapq.heappush(max_heap, -(first-sec))
        
        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]

        