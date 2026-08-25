class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return True
        
        