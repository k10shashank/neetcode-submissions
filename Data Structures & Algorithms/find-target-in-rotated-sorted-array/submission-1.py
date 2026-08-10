class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif target == nums[low]:
                return low
            elif target == nums[high]:
                return high
            elif nums[mid] <= nums[high] and nums[mid] >= nums[low]:
                if target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high] and nums[mid] <= nums[low]:
                if target > nums[mid] and target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] >= nums[high] and nums[mid] >= nums[low]:
                if target < nums[mid] and target > nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1
