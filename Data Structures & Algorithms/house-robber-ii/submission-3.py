class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums[0], nums[1])

        maxRob = []
        for idx in range(N-1):
            if idx == 0 or idx == 1:
                maxRob.append(nums[idx])
            elif idx == 2:
                maxRob.append(maxRob[idx-2] + nums[idx])
            else:
                maxRob.append(max(maxRob[idx-2], maxRob[idx-3]) + nums[idx])
        
        maxRob2 = []
        nums2 = nums[1:]
        for idx in range(N-1):
            if idx == 0 or idx == 1:
                maxRob2.append(nums2[idx])
            elif idx == 2:
                maxRob2.append(maxRob2[idx-2] + nums2[idx])
            else:
                maxRob2.append(max(maxRob2[idx-2], maxRob2[idx-3]) + nums2[idx])

        return max(maxRob[-1], maxRob[-2], maxRob2[-1], maxRob2[-2])
        