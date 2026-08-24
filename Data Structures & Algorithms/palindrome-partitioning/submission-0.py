class Solution:
    result = None
    word = None

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.word = s
        self.backtrack([s[0]], 1)
        return self.result

    def backtrack(self, current, index):
        if index == len(self.word):
            for curr in current:
                if len(curr) > 1 and not isPalindrome(curr):
                    return
            self.result.append(current)
            return
        
        self.backtrack(current + [self.word[index]], index + 1)
        self.backtrack(current[:-1] + [current[-1] + self.word[index]], index + 1)

def isPalindrome(word):
    i, j = 0, len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True
