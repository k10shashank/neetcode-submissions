class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ''
        N = len(s)
        for idx in range(N):
            l, r = idx, idx
            while l >= 0 and r <= N-1 and s[l] == s[r]:
                if r-l+1 > len(output):
                    output = s[l:r+1]
                l -= 1
                r += 1
        
        for idx in range(N-1):
            l, r = idx, idx+1
            while l >= 0 and r <= N-1 and s[l] == s[r]:
                if r-l+1 > len(output):
                    output = s[l:r+1]
                l -= 1
                r += 1
        
        return output
        