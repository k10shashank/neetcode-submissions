from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp = []
        heapq.heapify(hp)
        for i in range(k):
            heapq.heappush(hp, (-nums[i], -i))
        output = [-hp[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(hp, (-nums[i], -i))
            while -hp[0][1] <= i - k:
                heapq.heappop(hp)
            
            output.append(-hp[0][0])
        
        return output
        