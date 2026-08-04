class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            num_to_search = target - nums[i]
            if dic.get(num_to_search) is not None:
                return [dic[num_to_search], i]
            else:
                dic[nums[i]] = i
        return []

        