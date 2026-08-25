class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        return self.backtrack(self.root, word)

    def backtrack(self, root: TrieNode, search: str) -> bool:
        if len(search) == 0:
            return root.endOfWord

        cur = root
        char = search[0]
        if char != '.':
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            return self.backtrack(cur.children[idx], search[1:])
        else:
            validIdx = [idx for idx in range(26) if cur.children[idx] is not None]
            output = False
            for idx in validIdx:
                output = output or self.backtrack(cur.children[idx], search[1:])
                if output:
                    return output
            return output
