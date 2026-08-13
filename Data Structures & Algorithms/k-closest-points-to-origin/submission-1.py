import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for pnt in points:
            distance = (pnt[0] ** 2 + pnt[1] ** 2) ** 0.5
            heapq.heappush(min_heap, (distance, pnt))

        output = []
        while len(min_heap) > 0 and k > 0:
            output.append(heapq.heappop(min_heap)[1])
            k -= 1
        return output
