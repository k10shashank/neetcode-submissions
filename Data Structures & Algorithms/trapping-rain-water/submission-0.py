class Solution:
    def trap(self, height: List[int]) -> int:
        suffix = [0] * len(height)
        prefix = [0] * len(height)

        max_suffix = 0
        for i in range(len(height)-1, -1, -1):
            suffix[i] = max_suffix
            if height[i] > max_suffix:
                max_suffix = height[i]
                
        max_prefix = 0
        result = 0
        for i in range(len(height)):
            prefix[i] = max_prefix
            if height[i] > max_prefix:
                max_prefix = height[i]
            result += max(min(prefix[i], suffix[i]) - height[i],0)

        return result
        