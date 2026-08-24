class Solution:
    result = None

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.backtrack(nums, 0, [], 0, target)
        return self.result
    
    def backtrack(self, nums, index, current, currSum, targetSum):
        if currSum == targetSum:
            self.result.append(current.copy())
            return

        if len(nums) == index or currSum > targetSum:
            return

        self.backtrack(nums, index + 1, current, currSum, targetSum)

        current.append(nums[index])
        self.backtrack(nums, index, current, currSum + nums[index], targetSum)
        current.pop()
        