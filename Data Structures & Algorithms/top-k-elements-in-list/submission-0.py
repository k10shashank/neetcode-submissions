import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        arr = []
        heapq.heapify(arr)
        for key in dic:
            heapq.heappush(arr, (-dic[key], key))
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(arr)[1])
        
        return output
    