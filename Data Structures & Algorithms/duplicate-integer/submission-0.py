class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dyct = dict()
        for i in nums:
            if dyct.get(i) is None:
                dyct[i] = i
            else:
                return True
        return False
        