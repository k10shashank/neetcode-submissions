class Solution:
    result = None
    digits = None
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        self.result = []
        self.digits = digits
        self.backtrack(0, '')
        return self.result

    def backtrack(self, index, current):
        if index == len(self.digits):
            self.result.append(current)
            return
        
        for chars in get_chars(self.digits[index]):
            self.backtrack(index + 1, current + chars)

def get_chars(digit):
    return {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }[digit]
