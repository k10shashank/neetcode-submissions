class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return chr(1001)
        return chr(1000).join(strs)

    def decode(self, s: str) -> List[str]:
        if s == chr(1001):
            return []
        return s.split(chr(1000))
