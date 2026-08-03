class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0
        dyct = dict()
        for end in range(len(s)):
            if dyct.get(s[end]) is None:
                dyct[s[end]] = end
                maxLength = max(maxLength, end - start + 1)
            else:
                while s[start] != s[end]:
                    dyct.pop(s[start])
                    start += 1
                dyct[s[end]] = end
                start += 1
        return maxLength
        