class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        hashSet.add(n)
        while True:
            n = self.digitSquareSum(n)
            if n == 1:
                return True
            if n in hashSet:
                return False
            else:
                hashSet.add(n)
    
    def digitSquareSum(self, n: int):
        output = 0
        while n > 0:
            output += (n % 10) ** 2
            n = n // 10
        return output
        