def isAnagram(s: str, t: str) -> bool:
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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_arr = []
        output = []
        idx = 0
        while idx < len(strs):
            arr = [strs[idx]]
            jdx = idx + 1
            while jdx < len(strs):
                if isAnagram(strs[idx], strs[jdx]):
                    arr.append(strs[jdx])
                    strs.pop(jdx)
                else:
                    jdx = jdx + 1
            output.append(arr)
            idx = idx + 1
        return output

