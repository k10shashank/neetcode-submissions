import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        
        maxStreak = 0
        currentStreak = 0
        lastValue = None
        value = None
        while len(nums) != 0:
            lastValue = value
            value = heapq.heappop(nums)

            if value == lastValue:
                continue
            elif lastValue is None or value == lastValue + 1:
                currentStreak += 1
                maxStreak = max(maxStreak, currentStreak)
            else:
                currentStreak = 1

        return maxStreak
