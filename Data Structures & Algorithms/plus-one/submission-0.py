class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        extra = 0

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i != 0:
                    digits[i-1] = digits[i-1] + 1
                else:
                    extra = 1
        
        if extra == 1:
            return [1] + digits
        else:
            return digits
        