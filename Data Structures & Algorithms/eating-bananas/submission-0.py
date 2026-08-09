import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        low, high = 1, max_pile
        output = None
        while low <= high:
            time_taken = 0
            banana_per_hour = (low + high) // 2
            for i in range(len(piles)):
                time_taken += math.ceil(piles[i] / banana_per_hour)
            
            if time_taken <= h:
                if output is None:
                    output = banana_per_hour
                else:
                    output = min(banana_per_hour, output)
                high = banana_per_hour - 1
            else:
                low = banana_per_hour + 1

        return output
