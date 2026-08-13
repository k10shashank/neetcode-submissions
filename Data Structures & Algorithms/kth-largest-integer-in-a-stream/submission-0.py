import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.nums, nums[i])
            if len(self.nums) > self.k:
                heapq.heappop(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
