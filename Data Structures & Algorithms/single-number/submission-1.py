class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for i in nums:
            output = output ^ i
        return output
        