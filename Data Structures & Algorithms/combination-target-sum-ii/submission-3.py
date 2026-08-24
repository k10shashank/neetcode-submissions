class Solution:
    result = None
    nums = None
    maxAllowed = None

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = set()
        self.nums = set()
        self.maxAllowed = dict()

        for val in candidates:
            self.nums.add(val)
            self.maxAllowed[val] = self.maxAllowed.get(val, 0) + 1

        self.nums = sorted(list(self.nums))

        self.backtrack(self.nums, 0, [], 0, target)
        return [list(i) for i in self.result]

    def backtrack(self, nums, index, current, currSum, targetSum):
        if currSum == targetSum:
            self.result.add(tuple(current.copy()))
            return

        if len(nums) == index or currSum > targetSum:
            return

        self.backtrack(nums, index + 1, current, currSum, targetSum)

        if get_count(current.copy(), nums[index]) + 1 > self.maxAllowed[nums[index]]:
            return

        current.append(nums[index])
        self.backtrack(nums, index, current, currSum + nums[index], targetSum)
        current.pop()


def get_count(arr, val):
    cnt = 0
    for idx in range(len(arr) - 1, -1, -1):
        if arr[idx] == val:
            cnt += 1
        else:
            break
    return cnt