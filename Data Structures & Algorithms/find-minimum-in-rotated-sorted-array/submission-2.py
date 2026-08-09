class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        if nums[high] >= nums[low]:
            return nums[low]
        while low != high:
            mid = (low + high) // 2

            if nums[mid] > nums[low]:
                low = mid
            elif nums[mid] < nums[high]:
                high = mid
            else:
                break
        return nums[mid+1]
        