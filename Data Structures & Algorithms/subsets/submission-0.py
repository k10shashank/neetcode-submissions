class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for i in nums:
            arr = output.copy()
            for j in range(len(arr)):
                arr[j] = arr[j] + [i]
            output = output + arr
        
        return output
        