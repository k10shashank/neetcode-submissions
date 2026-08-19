class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        maxRob = []
        for idx in range(N):
            if idx == 0 or idx == 1:
                maxRob.append(nums[idx])
            elif idx == 2:
                maxRob.append(maxRob[idx - 2] + nums[idx])
            else:
                maxRob.append(max(maxRob[idx - 2], maxRob[idx - 3]) + nums[idx])
        return max(maxRob[N-1], maxRob[N-2])
        