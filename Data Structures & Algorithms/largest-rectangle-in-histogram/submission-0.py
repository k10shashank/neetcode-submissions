class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_small = [-1] * len(heights)
        stk = []
        for i in range(len(heights)):
            while len(stk) != 0 and stk[-1][0] >= heights[i]:
                stk.pop()
            if len(stk) != 0:
                prev_small[i] = stk[-1][1]
            stk.append((heights[i], i))
        
        next_small = [len(heights)] * len(heights)
        stk = []
        max_area = 0
        for i in range(len(heights) - 1, -1, -1):
            while len(stk) != 0 and stk[-1][0] >= heights[i]:
                stk.pop()
            if len(stk) != 0:
                next_small[i] = stk[-1][1]
            stk.append((heights[i], i))

            area = (next_small[i] - prev_small[i] - 1) * heights[i]
            max_area = max(area, max_area)

        return max_area
        