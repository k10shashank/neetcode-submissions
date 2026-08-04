class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_flag = 0
        for i in nums:
            if i != 0:
                product = product * i
            else:
                zero_flag += 1
                if zero_flag >= 2:
                    break
        
        output = []
        for i in range(len(nums)):
            if zero_flag >= 2:
                output.append(0)
            elif zero_flag == 1:
                if nums[i] == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(int(product/nums[i]))
        
        return output
        