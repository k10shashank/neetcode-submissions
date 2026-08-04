class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        if len(s) != len(t):
            return False
        for i in s:
            if d.get(i) is None:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        
        for i in t:
            if d.get(i) is None:
                return False
            elif d[i] > 1:
                d[i] = d[i] - 1
            else:
                d.pop(i)
        
        return True
        