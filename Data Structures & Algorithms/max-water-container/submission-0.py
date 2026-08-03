class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            minHeight = min(heights[left], heights[right])
            currArea = minHeight * (right - left)
            if currArea > maxArea:
                maxArea = currArea
            while left < right and heights[left] <= minHeight:
                left += 1
            while left < right and heights[right] <= minHeight:
                right -= 1
        
        return maxArea