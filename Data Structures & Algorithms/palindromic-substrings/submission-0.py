class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        N = len(s)
        for idx in range(N):
            l, r = idx, idx
            while l >= 0 and r <= N-1 and s[l] == s[r]:
                output += 1
                l -= 1
                r += 1
        
        for idx in range(N-1):
            l, r = idx, idx+1
            while l >= 0 and r <= N-1 and s[l] == s[r]:
                output += 1
                l -= 1
                r += 1
        
        return output
        