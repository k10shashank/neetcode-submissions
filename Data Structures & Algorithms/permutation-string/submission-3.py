class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = dict()
        for i in range(len(s1)):
            s1_chars[s1[i]] = s1_chars.get(s1[i], 0) + 1

        for start in range(len(s2) - len(s1) + 1):
            if s1_chars.get(s2[start]) is not None:
                end = start
                s1_chars_copy = s1_chars.copy()
                while end - start + 1 <= len(s1) and s1_chars_copy.get(s2[end]) is not None:
                    if s1_chars_copy[s2[end]] > 1:
                        s1_chars_copy[s2[end]] = s1_chars_copy[s2[end]] - 1
                    else:
                        s1_chars_copy.pop(s2[end])
                    end += 1
                if len(s1_chars_copy) == 0:
                    return True

        return False
        