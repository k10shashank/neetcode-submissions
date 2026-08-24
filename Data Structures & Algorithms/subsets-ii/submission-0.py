class Solution:
    result = None

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        nums.sort()
        self.backtrack(nums, 0, [])
        return [list(val) for val in self.result]

    def backtrack(self, nums, index, current):
        if index == len(nums):
            self.result.add(tuple(current.copy()))
            return

        self.backtrack(nums, index + 1, current)
        self.backtrack(nums, index + 1, current + [nums[index]])
        