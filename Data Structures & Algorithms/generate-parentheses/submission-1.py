class Solution:
    result = None
    N = None

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = set()
        self.N = n
        nums = '()' * n
        self.backtrack('', 0, 0)
        return list(self.result)

    def backtrack(self, current, currPlus, currMinus):
        if currPlus == self.N and currMinus == self.N:
            self.result.add(current)
            return
        
        if currPlus > self.N or currMinus > currPlus:
            return

        self.backtrack(current + '(', currPlus + 1, currMinus)
        self.backtrack(current + ')', currPlus, currMinus + 1)
