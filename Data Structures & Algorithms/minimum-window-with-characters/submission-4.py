class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars_freq = dict()
        s_chars_freq = dict()
        for s_char in s:
            s_chars_freq[s_char] = s_chars_freq.get(s_char, 0) + 1

        for t_char in t:
            t_chars_freq[t_char] = t_chars_freq.get(t_char, 0) + 1
            if s_chars_freq.get(t_char) is None:
                return ""
            elif s_chars_freq.get(t_char) > 1:
                s_chars_freq[t_char] = s_chars_freq[t_char] - 1
            else:
                s_chars_freq.pop(t_char)
        
        substring = s
        for start in range(len(s)):
            if s[start] in t:
                t_chars_freq_copy = t_chars_freq.copy()
                end = start
                while len(t_chars_freq_copy) != 0 and end < len(s):
                    if t_chars_freq_copy.get(s[end], 0) > 1:
                        t_chars_freq_copy[s[end]] = t_chars_freq_copy[s[end]] - 1
                    elif t_chars_freq_copy.get(s[end], 0) == 1:
                        t_chars_freq_copy.pop(s[end])
                    end += 1
                if len(t_chars_freq_copy) == 0 and (end - start) < len(substring):
                    substring = s[start:end]
        return substring
        