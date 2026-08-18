class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n > 0:
            output += n % 2
            n = n // 2
        return output
        