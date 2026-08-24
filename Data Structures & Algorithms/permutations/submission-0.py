class Solution:
    result = None
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(nums, 1, [nums[0]])
        return self.result

    def backtrack(self, nums, index, current):
        if len(current) == len(nums):
            self.result.append(current.copy())
            return

        if len(nums) == index:
            return

        for i in range(len(current)+1):
            self.backtrack(nums, index + 1, current[0:i] + [nums[index]] + current[i:])
        