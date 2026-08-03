class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValueAfter = [0] * len(prices)
        maxValue = 0
        for i in range(len(prices)-1,-1,-1):
            maxValueAfter[i] = maxValue
            maxValue = max(maxValue, prices[i])
        
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, maxValueAfter[i]-prices[i])
        
        return maxProfit
        