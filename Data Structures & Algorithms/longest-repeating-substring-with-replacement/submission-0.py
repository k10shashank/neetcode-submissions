class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        dyct = dict()
        maxLength = 0
        maxCharFreq = 0

        for end in range(len(s)):
            dyct[s[end]] = dyct.get(s[end], 0) + 1
            maxCharFreq = max(maxCharFreq, dyct[s[end]])

            while (end - start + 1) - maxCharFreq > k:
                dyct[s[start]] = dyct[s[start]] - 1
                start += 1
            
            maxLength = max(maxLength, (end - start + 1))
        
        return maxLength
        